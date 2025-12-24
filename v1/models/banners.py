from .base import BaseModel
from django.db import models

class BannersModel(BaseModel):
    title = models.CharField(max_length=255)
    text = models.TextField()
    background_image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return self.title