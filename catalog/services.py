from catalog.models import Category
from django.core.cache import cache


def get_categories():
    """
    Возвращает queryset со списком категорий
    """
    categories_list = cache.get('categories')
    if categories_list is None:
        categories_list = Category.objects.all()
        cache.set('categories', categories_list, 60)
    return categories_list
