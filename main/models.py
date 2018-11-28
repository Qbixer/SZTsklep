from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Price(models.Model):
    product_name = models.CharField(max_length=200)
    prices = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])