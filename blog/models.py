from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=255)
    content = models.TextField(verbose_name='Cодержимое')
    preview = models.ImageField(upload_to='preview/', verbose_name='Превью статьи')
    date_of_creation = models.DateTimeField(verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='Признак публикации')
    count_of_view = models.IntegerField(verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        """
        Класс для представления категорий во множественном и единственном числе
        """
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
