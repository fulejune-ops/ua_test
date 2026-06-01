from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я клієнта")
    email = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders', verbose_name="Клієнт")
    products = models.ManyToManyField(Product, related_name='orders', verbose_name="Товари")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Сума замовлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return f"Замовлення №{self.id} (Клієнт: {self.client.name})"