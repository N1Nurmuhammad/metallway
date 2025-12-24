from .base import BaseModel
from django.db import models
from .product_category import ProductsCategoryModel

class ProductsModel(BaseModel):

    class UnitsChoices(models.TextChoices):
        per_ton = "per_ton"
        per_kg = "per_kg"
        per_metr = "per_metr"
    image = models.ImageField(upload_to='products')
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(ProductsCategoryModel, on_delete=models.CASCADE, )
    units = models.CharField(choices=UnitsChoices.choices, max_length=20)
    standard = models.CharField(max_length=20)
    # tonn_to_metr = models.FloatField(null=True, blank=True)
    # metr_to_tonn = models.FloatField(null=True, blank=True)
    is_in_stock = models.BooleanField(default=False)


    def __str__(self):
        return self.name