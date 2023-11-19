from django.db import models


# #
#     наименование,
#     описание,
#     изображение (превью),
#     категория,
#     цена за штуку,
#     дата создания,
#     дата последнего изменения.
#
# Category:
#
#     наименование,
#     описание.

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=255, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение')
    catgory = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    date_of_creation = models.DateField(auto_now=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(verbose_name='дата изменения')

    def __str__(self):
        return f'{self.title}' \
               f'{self.description}' \
               f'{self.catgory}' \
               f'{self.price}' \
               f'{self.date_of_creation}' \
               f'{self.last_modified_date}'


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=255, verbose_name='описание')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'{self.title}'
                f'{self.description}')
