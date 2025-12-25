from django.db import models
from parler.models import TranslatableModel


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TranslatableBaseModel(TranslatableModel, BaseModel):
    class Meta:
        abstract = True