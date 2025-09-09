
from rest_framework import serializers
from .models import Store, Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'comment', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'store', 'name', 'description', 'price', 'image', 'reviews']


class StoreSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Store
        fields = ['id', 'vendor', 'name', 'description', 'logo', 'products']
