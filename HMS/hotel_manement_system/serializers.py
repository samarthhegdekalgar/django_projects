from rest_framework import serializers
from .models import Category, Guest


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('type', 'price',)


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('name', 'phone_no', 'adhar_number')
