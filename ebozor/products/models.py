from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, verbose_name="Telegram Username")
    telegram_id = models.BigIntegerField(unique=True, verbose_name="Telegram ID")

    def __str__(self):
        return f"{self.id}. {self.telegram_id} - {self.full_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name="Name")
    photo = models.CharField(max_length=255, null=True, verbose_name="Photo ID")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True)

    category_code = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    subcategory_code = models.CharField(max_length=50)
    subcategory_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"№{self.id} - {self.product_name}"
