from django.db import models
from parler.models import TranslatedFields
from .base import TranslatableBaseModel

class BannersModel(TranslatableBaseModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, null=True, blank=True),
        text=models.TextField(null=True, blank=True),
    )
    background_image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return self.title or ""