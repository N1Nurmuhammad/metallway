from .base import BaseModel
from django.db import models


class AboutUsModel(BaseModel):
    title = models.CharField(max_length=100)
    text = models.TextField()
    icon = models.ImageField(upload_to='icons')
    def __str__(self):
        return self.title


