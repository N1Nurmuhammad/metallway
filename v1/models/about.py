from django.db import models
from parler.models import TranslatedFields
from .base import TranslatableBaseModel


class AboutUsModel(TranslatableBaseModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100, null=True, blank=True),
        text=models.TextField(null=True, blank=True),
    )
    icon = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.title or ""


