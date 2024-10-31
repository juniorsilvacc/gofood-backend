from rest_framework import serializers
from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('O nome precisa ter pelo menos 3 caracteres.')
        return value
