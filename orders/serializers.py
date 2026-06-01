from rest_framework import serializers
from .models import Client, Product, Order


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Ціна товару повинна бути більшою за нуль.")
        return value


class OrderCreateSerializer(serializers.ModelSerializer):
    product_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'client', 'product_ids', 'total_amount']
        read_only_fields = ['total_amount']

    def validate_product_ids(self, value):
        # Бізнес-правило 2: у замовленні має бути хоча б один товар
        if not value:
            raise serializers.ValidationError("У замовленні має бути хоча б один товар.")
        return value

    def create(self, validated_data):
        product_ids = validated_data.pop('product_ids')
        client = validated_data['client']  # Бізнес-правило 1 гарантується DRF (Поле є обов'язковим)

        # Перевірка наявності товарів в базі даних
        products = Product.objects.filter(id__in=product_ids)
        if len(products) != len(set(product_ids)):
            raise serializers.ValidationError("Один або кілька обраних товарів не знайдено в системі.")

        # Бізнес-правило 3: автоматичний підрахунок суми замовлення
        total_amount = sum(product.price for product in products)

        order = Order.objects.create(client=client, total_amount=total_amount)
        order.products.set(products)
        return order


class OrderListSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'client', 'products', 'total_amount', 'created_at']