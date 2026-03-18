from django.urls import path
from new_project.catalog.apps import CatalogConfig
from new_project.catalog.views import home

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home')
]