"""products URL Configuration"""

from django.urls import path

from .views import (
    ProductListView,
    ProductDetailSlugView,
    )

app_name = "products"

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('/<str:slug>', ProductDetailSlugView.as_view(), name="detail")
]
