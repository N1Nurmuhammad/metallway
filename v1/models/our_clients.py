from .base import BaseModel
from django.db import models



class OurClientsModel(BaseModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logos")
    def __str__(self):
        return self.name