from rest_framework import serializers
from orders.models import Coupon, Address


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
