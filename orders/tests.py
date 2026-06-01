from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Client, Product


class OrderBusinessRulesTests(APITestCase):
    def setUp(self):
        self.client_user = Client.objects.create(name="ТОВ Компанія", email="info@company.com")
        self.product_1 = Product.objects.create(name="Серверна стійка", price=15000.00)
        self.product_2 = Product.objects.create(name="Маршрутизатор", price=5000.50)

    def test_create_order_success_and_auto_sum(self):
        url = reverse('create-order')
        data = {
            "client": self.client_user.id,
            "product_ids": [self.product_1.id, self.product_2.id]
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Сума має порахуватися автоматично: 15000.00 + 5000.50 = 20000.50
        self.assertEqual(float(response.data['total_amount']), 20000.50)

    def test_create_order_fails_without_products(self):
        url = reverse('create-order')
        data = {
            "client": self.client_user.id,
            "product_ids": []
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('product_ids', response.data)