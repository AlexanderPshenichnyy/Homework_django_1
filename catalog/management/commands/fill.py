from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories_list = [
            {'name': 'Одежда для животных', 'description': 'Широкий ассортимент'},
            {'name': 'Холодное оружие', 'description': 'Широкий ассортимент'},
            {'name': 'Соседи', 'description': 'Широкий ассортимент'}
        ]

        product_list = [
            {'name': 'Геннадий', 'description': 'Сосед Геннадий - отличается умом и сообразительностью',
             'category_id': 2,
             'price': 1000},
            {'name': 'Пырялка-3000', 'description': 'Штык-нож', 'category_id': 1, 'price': 2000},
            {'name': 'Свитер для питона', 'description': 'Вязаный свитер для вашего питона', 'category_id': 1,
             'price': 10_000},
            {'name': 'Пакет с прорезями', 'description': 'Просто отдайте коту', 'category_id': 1, 'price': 50},
            {'name': 'Пусковая установка земля-земля', 'description': 'Запускать только с воздуха', 'category_id': 1,
             'price': 50_000}
        ]

        for category_item in categories_list:
            Category.objects.create(**category_item)

        products_for_create = []
        for product_item in product_list:
            category_id = product_item.pop('category_id')
            category = Category, pk=category_id
            product_item['category'] = category
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
