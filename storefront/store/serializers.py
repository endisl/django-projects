from decimal import Decimal
from itertools import product
from rest_framework import serializers
from django.db.models.aggregates import Count
from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.SerializerMethodField(
        method_name='collection_inventory')

    def collection_inventory(self, collection: Collection):
        # count = Product.objects.filter(
        #    collection__id=collection.id).aggregate(Count('id'))
        return collection.products.count()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
