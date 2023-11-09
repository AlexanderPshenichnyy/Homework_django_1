from django.urls import path
from catalog.views import homepage
from catalog.views import contacts


urlpatterns = [
    path('', homepage),
    path('contacts/', contacts)
]
