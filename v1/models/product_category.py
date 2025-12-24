
from .base import BaseModel
from django.db import models


class ProductsCategoryModel(BaseModel):
    image = models.ImageField(upload_to='products_category')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name