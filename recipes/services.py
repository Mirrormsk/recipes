import time

from django.db import transaction, DatabaseError
from django.db.models import F

from recipes.models import Recipe, Product


class RecipeService:
    @staticmethod
    def increment_ingredients_usage_counters(recipe: Recipe):
        """Increments the recipe ingredients usage counters

        :param recipe: Recipe instance
        :type recipe: Recipe
        :return: None
        """
        used_products_ids = recipe.ingredients.values_list("product_id", flat=True)
        with transaction.atomic():
            Product.objects.filter(pk__in=used_products_ids).select_for_update().update(
                usage_count=F("usage_count") + 1
            )
