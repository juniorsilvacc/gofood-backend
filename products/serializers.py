from rest_framework import serializers
from products.models import Product
from categories.serializers import CategorySerializer
import re


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('O nome precisa ter pelo menos 3 caracteres.')
        elif not re.match("^[A-Za-z0-9_]*$", value):
            raise serializers.ValidationError('O nome pode conter apenas letras, números e sublinhados.')
        return value

    def create(self, validated_data):
        # Recupera o nome dos dados validados
        name = validated_data.get('name')
        if Product.objects.filter(name=name).exists():
            raise serializers.ValidationError({"name": "Já existe um produto com esse nome."})
        return super().create(validated_data)

    def validate_price(self, value):
        if value < 1:
            raise serializers.ValidationError('O preço do produto precisa ser maior que 0.')
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('O nome precisa ter pelo menos 10 caracteres.')
        return value

    def validate_image(self, value):
        if value:
            if not value.name.endswith(('.png', '.jpg', '.jpeg')):
                raise serializers.ValidationError('A imagem deve ser em formato PNG ou JPG.')
        return value


class ProductListDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'ingredients', 'price', 'image', 'active', 'category', 'additionals']
