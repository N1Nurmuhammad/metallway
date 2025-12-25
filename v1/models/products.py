from django.db import models
from parler.models import TranslatedFields
from .base import TranslatableBaseModel
from .product_category import ProductsCategoryModel

class ProductsModel(TranslatableBaseModel):

    class UnitsChoices(models.TextChoices):
        per_ton = "per_ton"
        per_kg = "per_kg"
        per_metr = "per_metr"

    image = models.ImageField(upload_to='products')
    price = models.PositiveIntegerField()
    category = models.ForeignKey(ProductsCategoryModel, on_delete=models.CASCADE)
    units = models.CharField(choices=UnitsChoices.choices, max_length=20)
    is_in_stock = models.BooleanField(default=False)

    translations = TranslatedFields(
        name=models.CharField(max_length=100, null=True, blank=True),
        standard=models.CharField(max_length=50, null=True, blank=True),
    )

    def __str__(self):
        return self.name or ""