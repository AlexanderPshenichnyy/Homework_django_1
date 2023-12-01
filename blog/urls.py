from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    # path('view/', ..., name='view'),
    # path('edit/', ..., name='edit'),
    # path('delete/', ..., name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
