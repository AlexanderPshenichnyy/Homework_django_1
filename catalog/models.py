from django.db import models

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
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(**NULLABLE, verbose_name='Цена')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        """
        Класс для представления категорий во множественном и единственном числе
        """
        verbose_name = 'Product'
        verbose_name_plural = 'Produts'
