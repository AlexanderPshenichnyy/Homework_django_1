from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories_list = [
            {'title': 'Одежда для животных', 'description': 'Широкий ассортимент'},
            {'title': 'Холодное оружие', 'description': 'Широкий ассортимент'},
            {'title': 'Соседи', 'description': 'Широкий ассортимент'}
        ]

        product_list = [
            {'title': 'Геннадий', 'description': 'Сосед Геннадий - отличается умом и сообразительностью',
             'category_id': 3,
             'price': 1000},
            {'title': 'Пырялка-3000', 'description': 'Штык-нож', 'category_id': 2, 'price': 2000},
            {'title': 'Свитер для питона', 'description': 'Вязаный свитер для вашего питона', 'category_id': 1,
             'price': 10_000},
            {'title': 'Пакет с прорезями', 'description': 'Просто отдайте коту', 'category_id': 1, 'price': 50},
            {'title': 'Пусковая установка земля-земля', 'description': 'Запускать только с воздуха', 'category_id': 2,
             'price': 50_000},
            {'title': 'Карандаш', 'description': 'Джон Уик, знает, что делать', 'category_id': 2,
             'price': 50_000}
        ]

        for category_item in categories_list:
            Category.objects.create(**category_item)

        products_for_create = []
        for product_item in product_list:
            category_id = product_item.pop('category_id')
            category = Category.objects.get(id=category_id)
            product_item['category'] = category
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
