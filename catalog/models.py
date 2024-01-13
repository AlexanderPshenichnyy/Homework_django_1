from django.db import models
from users.models import User

NULLABLE = {
    'null': True, 'blank': True
}


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=255, **NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(blank=True, upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(**NULLABLE, verbose_name='Цена')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Produts'

        permissions = [
            (
                'set_published_status',
                'Can publish products'
            ),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number_of_version = models.PositiveIntegerField(verbose_name='Номер версии')
    title_of_version = models.CharField(max_length=255, **NULLABLE, verbose_name='Название версии')
    sign_is_active = models.BooleanField(default=False, verbose_name='Признак версии')

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Versions'
