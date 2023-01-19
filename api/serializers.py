from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            'id',
            'bank_name'
        ]
        depth=1


class Bank_used_by_ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            'id',
            'bank_name'
        ]


class ProviderSerializer(serializers.ModelSerializer):
    bank=Bank_used_by_ProviderSerializer(many=True, read_only=True)
    class Meta:
        model = Provider
        fields = [
            'id',
            'provider_name',
            'nit_provider',
            'contact_name',
            'cell_phone_contact',
            'bank'
        ]
        depth=1


class Provider_userby_BankAccountSerializer(
        serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            'id',
            'provider_name'
        ]


class Bank_used_by_BankAccountSerializer(
        serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            'id',
            'bank_name'
        ]


class BankAccountreadonlySerializer(serializers.ModelSerializer):
    provider = Provider_userby_BankAccountSerializer(many=False, read_only=True)
    bank = Bank_used_by_BankAccountSerializer(many = False, read_only=True)
    class Meta:
        model = BankAccount
        fields = [
            'id',
            'provider',
            'bank',
            'bank_account_number'
        ]


class BankAccountSerializer(serializers.ModelSerializer):
    provider = serializers.PrimaryKeyRelatedField(many=False, queryset=Provider.objects.all())
    bank=serializers.PrimaryKeyRelatedField(many = False, queryset=Bank.objects.all())
    class Meta:
        model = BankAccount
        fields = [
            'id',
            'provider',
            'bank',
            'bank_account_number'
        ]
