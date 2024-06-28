from rest_framework import serializers
from .models import ProductData, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image", "caption"]
        # fields = ['image']


class ProductMetaDataSerializer(serializers.ModelSerializer):
    # images = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProductData
        fields = [
            "id",
            "product_summary",
            "product_categories",
            "product_rating",
            "product_name",
            "product_unique_id",
            "product_url",
            "product_featured",
            "images",
        ]

class ProductDataSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProductData
        fields = [
            "id",
            "product_summary",
            "product_categories",
            "product_pros",
            "product_cons",
            "product_usecases",
            "product_toolfor",
            "product_pricing",
            "product_rating",
            "product_name",
            "product_unique_id",
            "product_pricing_available",
            "product_affiliate_available",
            "product_featured",
            "product_url",
            "images",
        ]
