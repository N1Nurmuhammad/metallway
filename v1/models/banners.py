from django.db import models
from parler.models import TranslatedFields
from .base import TranslatableBaseModel

class BannersModel(TranslatableBaseModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        text=models.TextField(),
    )
    background_image = models.ImageField(upload_to="banners/")

    def __str__(self):
        return self.title