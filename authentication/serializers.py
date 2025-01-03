from rest_framework import serializers
from django.contrib.auth.models import User, Group


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    telephone = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'telephone']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("O nome de usuário já está em uso.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("O email já está em uso.")
        return value

    def create(self, validated_data):
        telephone = validated_data.pop('telephone')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )

        # Salvar o telefone no perfil
        user.profile.telephone = telephone
        user.profile.save()

        # Adicionar o usuário a um grupo
        group_name = 'user_standard'

        try:
            # Busque o grupo pelo nome e adicione o usuário
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
        except Group.DoesNotExist:
            raise serializers.ValidationError(f'O grupo {group_name} não existe.')

        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['telephone'] = instance.profile.telephone
        return representation
