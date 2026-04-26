from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    is_low_stock = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative")
        return value

    def validate(self, data):
        if data.get("name") == "":
            raise serializers.ValidationError("Name is required")
        return data