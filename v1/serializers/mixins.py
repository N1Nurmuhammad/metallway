from rest_framework import serializers
from parler.utils.context import switch_language

from v1.utils.i18n import SUPPORTED_LANGS


class TranslatableFieldsSerializerMixin(serializers.ModelSerializer):
    """
    Mixin to add a `translations` field for django-parler TranslatableModel instances.

    Usage:
    - Define `translatable_fields` on the serializer (tuple/list of translated field names).
    - Include "translations" in the serializer Meta.fields to expose all languages.
    """

    translations = serializers.SerializerMethodField()

    # Override in subclasses: e.g. ("title", "text")
    translatable_fields: tuple[str, ...] = tuple()

    def get_translations(self, obj):
        result = {}
        for lang in SUPPORTED_LANGS:
            with switch_language(obj, lang):
                result[lang] = {fname: getattr(obj, fname, None) for fname in self.translatable_fields}
        return result
