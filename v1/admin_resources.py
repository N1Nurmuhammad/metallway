from django.conf import settings
from import_export import fields, resources

from v1.models import (
    AboutUsModel,
    BannersModel,
    OurClientsModel,
    ProductsCategoryModel,
    ProductsModel,
)


class TranslatedModelResource(resources.ModelResource):
    """Adds one column per language for each translatable field."""

    translatable_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._translation_field_map = {}
        language_codes = [code for code, _ in settings.LANGUAGES]

        for field_name in self.translatable_fields:
            for lang in language_codes:
                column = f"{field_name}_{lang}"
                if column not in self.fields:
                    self.fields[column] = fields.Field(column_name=column)
                self._translation_field_map[column] = (field_name, lang)

        # If no explicit export order was set, include new fields in insertion order
        if not getattr(self._meta, "export_order", None):
            self._meta.export_order = tuple(self.fields.keys())

    def export_field(self, field, instance, **kwargs):
        name = self.get_field_name(field)
        if name in self._translation_field_map:
            base_field, lang = self._translation_field_map[name]
            return instance.safe_translation_getter(base_field, language_code=lang, any_language=False)
        return super().export_field(field, instance, **kwargs)

    def import_field(self, field, obj, data, is_m2m=False, **kwargs):
        name = self.get_field_name(field)
        if name in self._translation_field_map:
            value = data.get(name)
            if value in (None, ""):
                return
            base_field, lang = self._translation_field_map[name]
            obj.set_current_language(lang)
            setattr(obj, base_field, value)
            return
        return super().import_field(field, obj, data, is_m2m=is_m2m, **kwargs)


class AboutUsResource(TranslatedModelResource):
    translatable_fields = ("title", "text")

    class Meta:
        model = AboutUsModel
        fields = ("id", "icon", "created_at", "updated_at")
        import_id_fields = ("id",)


class BannersResource(TranslatedModelResource):
    translatable_fields = ("title", "text")

    class Meta:
        model = BannersModel
        fields = ("id", "background_image", "created_at", "updated_at")
        import_id_fields = ("id",)


class ProductsCategoryResource(TranslatedModelResource):
    translatable_fields = ("name",)

    class Meta:
        model = ProductsCategoryModel
        fields = ("id", "image", "created_at", "updated_at")
        import_id_fields = ("id",)


class ProductsResource(TranslatedModelResource):
    translatable_fields = ("name", "standard")

    class Meta:
        model = ProductsModel
        fields = (
            "id",
            "category",
            "price",
            "units",
            "is_in_stock",
            "image",
            "created_at",
            "updated_at",
        )
        import_id_fields = ("id",)


class OurClientsResource(TranslatedModelResource):
    translatable_fields = ("name",)

    class Meta:
        model = OurClientsModel
        fields = ("id", "logo", "created_at", "updated_at")
        import_id_fields = ("id",)
