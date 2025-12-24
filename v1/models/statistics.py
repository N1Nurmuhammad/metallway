from .base import BaseModel
from django.db import models
from .product_category import ProductsCategoryModel

class StatisticsModel(BaseModel):
    delivered = models.PositiveIntegerField(default=5000)
    happy_clients = models.PositiveIntegerField(default=1000)
    year_experience = models.PositiveIntegerField(default=10)
    specialists = models.PositiveIntegerField(default=150)
    customer_support = models.CharField(max_length=100, default="24/7")


    def __str__(self):
        return f"statistics {self.id}"