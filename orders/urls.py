from django.urls import path
from .views import ClientCreateView, ProductCreateView, OrderCreateView, ClientOrderListView

urlpatterns = [
    path('clients/', ClientCreateView.as_view(), name='create-client'),
    path('products/', ProductCreateView.as_view(), name='create-product'),
    path('orders/', OrderCreateView.as_view(), name='create-order'),
    path('clients/<int:client_id>/orders/', ClientOrderListView.as_view(), name='client-orders'),
]