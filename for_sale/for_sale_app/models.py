from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    PRODUCT_CATEGORIES = [
        ('HB', 'Health and beauty'),
        ('OTHER', 'Other'),
        ('ELEC', 'Electronics'),
        ('HOME', 'Home'),
        ('SPORT', 'Sports and exercise'),
        ('ENTER', 'Entertainment'),
        ('FOOD', 'Food'),
        ('BOOK', 'Books'),
    ]

    # left is stored in database, right is what's displayed

    category = models.CharField(max_length=5, choices=PRODUCT_CATEGORIES, default='OTHER')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    picture = models.ImageField(default='images/default.jpg', null=True, upload_to='images/', blank=True, )
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("for_sale_app:product-detail", kwargs={"my_id": self.id})
