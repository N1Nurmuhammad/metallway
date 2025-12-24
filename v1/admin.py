from django.contrib import admin

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
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    ordering = ("-id",)


@admin.register(BannersModel)
class BannersAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)
    ordering = ("-id",)


@admin.register(ProductsCategoryModel)
class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(ProductsModel)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "units", "is_in_stock", "created_at")
    list_filter = ("category", "units", "is_in_stock")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(LeadModel)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_at")
    search_fields = ("name", "email")
    ordering = ("-created_at",)


@admin.register(StatisticsModel)
class StatisticsAdmin(admin.ModelAdmin):
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
class OurClientsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)
