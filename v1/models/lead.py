from .base import BaseModel
from django.db import models
from .products import ProductsModel

class LeadModel(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    products = models.ManyToManyField(to=ProductsModel)
    comment = models.TextField(null=True, blank=True)


