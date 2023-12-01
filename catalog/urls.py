from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]
