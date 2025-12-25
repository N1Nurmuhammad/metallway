from django.db import models
from parler.models import TranslatedFields
from .base import TranslatableBaseModel


class OurClientsModel(TranslatableBaseModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
    )
    logo = models.ImageField(upload_to="logos")

    def __str__(self):
        return self.name