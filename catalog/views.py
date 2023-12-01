from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/homepage.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


def contacts(request):
    return render(request, 'catalog/contacts.html', {'title': 'Контакты'})
