from rest_framework import generics
from .models import Client, Product, Order
from .serializers import ClientSerializer, ProductSerializer, OrderCreateSerializer, OrderListSerializer


class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        return OrderListSerializer


class ClientOrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        # Використовуємо prefetch_related для оптимізації SQL-запитів (уникнення проблеми N+1)
        return Order.objects.filter(client_id=client_id).prefetch_related('products', 'client')