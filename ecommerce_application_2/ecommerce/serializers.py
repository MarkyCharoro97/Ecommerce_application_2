from rest_framework import serializers
from .models import Store, Product, Review

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["id", "name", "description", "logo", "address", "phone_number", "email", "is_active"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "store", "name", "description", "price", "quantity_in_stock", "is_active", "image"]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "product", "buyer", "rating", "comment", "created_at"]
