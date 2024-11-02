from rest_framework import serializers
from products.models import Product
from orders.models import Coupon, Address, Order, OrderItem


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

    def validate_code(self, value):
        if not value.islnum():
            raise serializers.ValidationError("O código deve conter apenas caracteres alfanuméricos.")
        if len(value) != 8:
            raise serializers.ValidationError("O código deve ter exatamente 8 caracteres.")
        return value

    def validate_discount(self, value):
        if value < 0 and value > 100:
            raise serializers.ValidationError("O desconto deve estar entre 0 e 100.")
        return value

    def validate_uses(self, value):
        if value < 0:
            raise serializers.ValidationError("O número de usos deve ser um número positivo.")
        return value


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def validate_zipe_code(self, value):
        if value and (not value.isdigit() or len(value) != 8):
            raise serializers.ValidationError("O CEP deve ter exatamente 8 dígitos numéricos.")
        return value

    def validate_number(self, value):
        if not value.islnum():
            raise serializers.ValidationError("O número deve ser alfanumérico.")

    def validate_street(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome da rua deve ter pelo menos 3 caracteres.")
        return value

    def validate_district(self, value):
        if value and (len(value) < 3):
            raise serializers.ValidationError("O bairro deve ter pelo menos 3 caracteres.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'total', 'change_due', 'coupon', 'address', 'payment']

    def validate_coupon(self, value):
        if value and not value.active:
            raise serializers.ValidationError("Este cupom não está mais ativo.")
        return value

    def validate_total(self, value):
        if value < 0:
            raise serializers.ValidationError("O valor total do pedido deve ser maior que zero.")
        return value

    def create(self, validated_data):
        coupon = validated_data.get('coupon')
        if coupon:
            discount = coupon.discount / 100
            validated_data['total'] *= (1 - discount)
            coupon.uses += 1
            coupon.save()
        return super().create(validated_data)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price', 'description']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("A quantidade deve ser maior que zero.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("O preço deve ser maior que zero.")
        return value

    def validate(self, data):
        order = data.get('order')
        product = data.get('product')

        if not Order.objects.filter(id=order.id).exists():
            raise serializers.ValidationError("O pedido especificado não existe.")

        if not Product.objects.filter(id=product.id).exists():
            raise serializers.ValidationError("O produto especificado não existe.")

        return data


class OrderDetailSerializer(serializers.ModelSerializer):
    coupon = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    items = OrderItemSerializer(many=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'total', 'change_due', 'coupon', 'address', 'payment', 'date', 'delivered', 'items', 'created_at', 'updated_at']

    def get_coupon(self, obj):
        if obj.coupon:
            return {"id": obj.coupon.id, "code": obj.coupon.code, "discount": obj.coupon.discount}
        return None

    def get_address(self, obj):
        if obj.address:
            return {
                "id": obj.address.id,
                "zip_code": obj.address.zip_code,
                "street": obj.address.street,
                "district": obj.address.district,
                "number": obj.address.number,
                "reference": obj.address.reference
            }
        return None
