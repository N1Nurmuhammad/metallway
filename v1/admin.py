from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from parler.admin import TranslatableAdmin

from v1.models import (
    AboutUsModel,
    BannersModel,
    ProductsCategoryModel,
    ProductsModel,
    LeadModel,
    StatisticsModel,
    OurClientsModel,
)


@admin.register(AboutUsModel)
class AboutUsAdmin(TranslatableAdmin, ImportExportModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("translations__title",)
    ordering = ("-id",)


@admin.register(BannersModel)
class BannersAdmin(TranslatableAdmin, ImportExportModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("translations__title",)
    ordering = ("-id",)


@admin.register(ProductsCategoryModel)
class ProductsCategoryAdmin(TranslatableAdmin, ImportExportModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("translations__name",)
    ordering = ("translations__name",)


@admin.register(ProductsModel)
class ProductsAdmin(TranslatableAdmin, ImportExportModelAdmin):
    list_display = ("id", "name", "category", "price", "units", "is_in_stock", "created_at")
    list_filter = ("category", "units", "is_in_stock")
    search_fields = ("translations__name", "translations__standard")
    ordering = ("translations__name",)


@admin.register(LeadModel)
class LeadAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "email", "created_at")
    search_fields = ("name", "email")
    ordering = ("-created_at",)


@admin.register(StatisticsModel)
class StatisticsAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "delivered",
        "happy_clients",
        "year_experience",
        "specialists",
        "customer_support",
        "created_at",
    )
    ordering = ("-id",)


@admin.register(OurClientsModel)
class OurClientsAdmin(TranslatableAdmin, ImportExportModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("translations__name",)
    ordering = ("translations__name",)
