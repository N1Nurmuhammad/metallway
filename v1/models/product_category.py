from django.db import models
from parler.models import TranslatedFields
from .base import TranslatableBaseModel


class ProductsCategoryModel(TranslatableBaseModel):
    image = models.ImageField(upload_to='products_category')
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
    )

    def __str__(self):
        return self.name