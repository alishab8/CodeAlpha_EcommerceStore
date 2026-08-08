from django.core.management.base import BaseCommand
from store.models import Category, Product


class Command(BaseCommand):
    help = "Seed the database with sample categories and products"

    def handle(self, *args, **options):
        categories = {
            "electronics": "Electronics",
            "clothing": "Clothing",
            "home-goods": "Home Goods",
        }
        cat_objs = {}
        for slug, name in categories.items():
            cat, _ = Category.objects.get_or_create(slug=slug, defaults={"name": name})
            cat_objs[slug] = cat

        products = [
            ("Wireless Headphones", "electronics", 59.99, 25, "Noise-cancelling over-ear headphones with 30h battery life."),
            ("Smart Watch", "electronics", 89.99, 15, "Fitness tracking smartwatch with heart-rate monitor."),
            ("Cotton T-Shirt", "clothing", 14.99, 100, "Soft, breathable 100% cotton t-shirt, unisex fit."),
            ("Denim Jacket", "clothing", 49.99, 30, "Classic denim jacket, machine washable."),
            ("Ceramic Mug Set", "home-goods", 19.99, 50, "Set of 4 handmade ceramic mugs."),
            ("Table Lamp", "home-goods", 34.99, 0, "Minimalist wooden base table lamp — currently out of stock."),
        ]

        for name, cat_slug, price, stock, desc in products:
            slug = name.lower().replace(" ", "-")
            Product.objects.get_or_create(
                slug=slug,
                defaults={
                    "name": name,
                    "category": cat_objs[cat_slug],
                    "price": price,
                    "stock": stock,
                    "description": desc,
                },
            )

        self.stdout.write(self.style.SUCCESS("Seed data created successfully."))
