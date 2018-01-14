from django.urls import path

from .views import SearchProductView

app_name = "products"

urlpatterns = [
    path('', SearchProductView.as_view(), name="query"),
]