import csv

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Import from csv'

    def handle(self, *args, **options):
        with open('recipes/data/ingredients.csv', encoding='utf-8') as a:
            reader = csv.reader(a)
            for row in reader:
                name, unit = row
                Ingredient.objects.get_or_create(
                    name=name, measurement_unit=unit)
        self.stdout.write(
            self.style.SUCCESS('Import from csv completed!'))