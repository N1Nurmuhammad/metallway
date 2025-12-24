from django.urls import path

from v1.views import (
    list_about_us, retrieve_about_us,
    list_banners, retrieve_banners,
    list_product_categories, retrieve_product_category,
    list_products, retrieve_products,
    list_leads, retrieve_lead,
    list_statistics, retrieve_statistics,
    list_our_clients, retrieve_our_client,
)

urlpatterns = [
    path("about-us/", list_about_us, name="about-us-list"),
    path("about-us/<int:pk>/", retrieve_about_us, name="about-us-detail"),

    path("banners/", list_banners, name="banners-list"),
    path("banners/<int:pk>/", retrieve_banners, name="banners-detail"),

    path("product-categories/", list_product_categories, name="product-categories-list"),
    path("product-categories/<int:pk>/", retrieve_product_category, name="product-categories-detail"),

    path("products/", list_products, name="products-list"),
    path("products/<int:pk>/", retrieve_products, name="products-detail"),

    path("leads/", list_leads, name="leads-list"),
    path("leads/<int:pk>/", retrieve_lead, name="leads-detail"),

    path("statistics/", list_statistics, name="statistics-list"),
    path("statistics/<int:pk>/", retrieve_statistics, name="statistics-detail"),

    path("our-clients/", list_our_clients, name="our-clients-list"),
    path("our-clients/<int:pk>/", retrieve_our_client, name="our-clients-detail"),
]
