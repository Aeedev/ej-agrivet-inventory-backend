from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default="Poultry")
    supplier = models.CharField(max_length=200, blank=True)

    stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)

    price_per_kg = models.FloatField(default=0)
    price_per_sack = models.FloatField(default=0)

    cost_price = models.FloatField(default=0)
    selling_price = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StockHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.change})"