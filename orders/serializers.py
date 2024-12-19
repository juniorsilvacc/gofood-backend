from rest_framework import serializers
from products.models import Product, Option
from orders.models import Coupon, Address, Order, OrderItem
from products.serializers import OptionSerializer


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

    def validate_zip_code(self, value):
        if value and (not value.isdigit() or len(value) != 8):
            raise serializers.ValidationError("O CEP deve ter exatamente 8 dígitos numéricos.")
        return value

    def validate_number(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("O número deve ser alfanumérico.")
        return value

    def validate_street(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome da rua deve ter pelo menos 3 caracteres.")
        return value

    def validate_district(self, value):
        if value and (len(value) < 3):
            raise serializers.ValidationError("O bairro deve ter pelo menos 3 caracteres.")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    options = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all(), many=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price', 'description', 'options']

    def get_options(self, obj):
        # Retorna apenas 'id' e 'name' das opções associadas ao produto
        product = obj.product  # O 'product' é uma ForeignKey em OrderItem
        if product:
            options = Option.objects.filter(id__in=obj.options.values_list('id', flat=True))
            return OptionSerializer(options, many=True).data  # Aqui estamos usando o OptionSerializer para incluir somente 'id' e 'name'
        return []  # Retorna uma lista vazia se não houver opções

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("A quantidade deve ser maior que zero.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("O preço deve ser maior que zero.")
        return value

    def validate(self, data):
        # Se o 'product' for fornecido, verifique se existe
        product = data.get('product')

        if not Product.objects.filter(id=product.id).exists():
            raise serializers.ValidationError("O produto especificado não existe.")

        return data


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total', 'change_due', 'coupon', 'address', 'payment', 'date', 'delivered', 'items', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate_coupon(self, value):
        if value and not value.active:
            raise serializers.ValidationError("Este cupom não está mais ativo.")
        return value

    def validate_total(self, value):
        if value < 0:
            raise serializers.ValidationError("O valor total do pedido deve ser maior que zero.")
        return value

    def create(self, validated_data):
        # Extrair itens do pedido
        items_data = validated_data.pop('items', [])
        # Criar o pedido
        order = Order.objects.create(**validated_data)
        # Criar os OrderItems e vinculá-los à Order
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        # Agora que o pedido foi salvo, calcular o total_value
        total_value = sum(item.get_total_price() for item in order.order_items.all())
        if order.coupon:
            total_value -= order.coupon.discount

        order.total_value = total_value
        order.save(update_fields=["total_value"])

        return order


class OrderDetailSerializer(serializers.ModelSerializer):
    coupon = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    items = OrderItemSerializer(source='order_items', many=True, read_only=True)

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
