from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('shirts', 'Shirts'),
        ('shorts', 'Shorts'),
        ('jackets', 'Jackets'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
