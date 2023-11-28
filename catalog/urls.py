from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', homepage),
    path('contacts/', contacts),
    path('products/', products)
]
