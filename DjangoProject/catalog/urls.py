from django.urls import path, include
from apps import CatalogConfig
from views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
