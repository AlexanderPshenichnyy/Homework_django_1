from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        categories_list = [
            {'title': 'Одежда для животных', 'description': 'Широкий ассортимент'},
            {'title': 'Холодное оружие', 'description': 'Широкий ассортимент'},
            {'title': 'Соседи', 'description': 'Широкий ассортимент'}
        ]

        cat0 = categories_list[0].get('title')
        cat1 = categories_list[1].get('title')
        cat2 = categories_list[2].get('title')

        product_list = [
            {'title': 'Геннадий',
             'description': 'Сосед Геннадий - отличается умом и сообразительностью. Любит сверлить в 5 утра,'
                            'увлекается музыкой, если игру на грустном тромбоне можно называть музыкой.',
             'category': cat2, 'price': 1000},
            {'title': 'Пырялка-3000', 'description': 'Нож', 'category': cat1, 'price': 2000},
            {'title': 'Сменная чешуя для питона', 'description': 'Чешуя для вашего питона', 'category': cat0,
             'price': 10_000},
            {'title': 'Пакет с прорезями', 'description': 'Просто отдайте коту', 'category': cat0, 'price': 50},
            {'title': 'Пусковая установка земля-земля', 'description': 'Запускать только с воздуха', 'category': cat1,
             'price': 50_000},
        ]

        for category_item in categories_list:
            Category.objects.create(**category_item)

        products_for_create = []

        for product_item in product_list:
            category = product_item.pop('category')
            category = Category.objects.get(title=category)
            product_item['category'] = category
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)
