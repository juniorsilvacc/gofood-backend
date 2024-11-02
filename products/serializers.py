from rest_framework import serializers
from products.models import Option
from products.models import Additional
from products.models import Product
import re


# Mixin para validações comuns
class NamValidationMixin:
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('O nome precisa ter pelo menos 3 caracteres.')
        elif not re.match("^[A-Za-z0-9_]*$", value):
            raise serializers.ValidationError('O nome pode conter apenas letras, números e sublinhados.')
        return value

    def check_name_uniqueness(self, model, name):
        if model.objects.filter(name=name).exists():
            raise serializers.ValidationError({"name": "Já existe um produto com esse nome."})


# Serializer Option
class OptionSerializer(NamValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

    def create(self, validated_data):
        self.check_name_uniqueness(Option, validated_data.get('name'))
        return super().create(validated_data)


# Serializer Additional
class AdditionalSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    
    class Meta:
        model = Additional
        fields = '__all__'


class AdditionalListDetailSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Additional
        fields = ['id', 'name', 'quantity_options', 'active', 'options']

    def get_options(self, obj):
        return [{"id": option.id, "name": option.name, "addition": option.addition} for option in obj.options.all()]


# Serializer Product
class ProductSerializer(NamValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        self.check_name_uniqueness(Product, validated_data.get('name'))
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
    category = serializers.SerializerMethodField()
    additionals = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'ingredients', 'price', 'image', 'active', 'category', 'additionals']

    def get_category(self, obj):
        if obj.category:
            return {"id": obj.category.id, "name": obj.category.name}
        return None

    def get_additionals(self, obj):
        return [
            {
                "name": additional.name,
                "quantity_options": additional.quantity_options,
                "options": [{"name": option.name, "addition": option.addition} for option in additional.options.all()]
            }
            for additional in obj.additionals.all()
        ]


class AdditionalOptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    options = serializers.ListField(
        child=serializers.IntegerField(), allow_empty=True
    )