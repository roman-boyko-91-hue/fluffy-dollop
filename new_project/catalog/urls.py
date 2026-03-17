from django.urls import path
from new_project.catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('',)
]