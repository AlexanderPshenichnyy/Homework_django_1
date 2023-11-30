from django.shortcuts import render
from catalog.models import Product


def homepage(request):
    return render(request, 'catalog/homepage.html', {'title': 'Главная страница'})


def contacts(request):
    return render(request, 'catalog/contacts.html', {'title': 'Контакты'})


def products(request):
    product_list = Product.objects.all()

    context = {
        'title': 'Товары',
        'object_list': product_list
    }
    return render(request, 'catalog/products.html', context)
