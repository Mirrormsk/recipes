import time

from django.db import transaction, DatabaseError

from recipes.models import Recipe


class RecipeService:
    @staticmethod
    def increment_ingredients_usage_counters(recipe: Recipe):
        """Increments the recipe ingredients usage counters

        :param recipe: Recipe instance
        :type recipe: Recipe
        :return: None
        """
        ingredients = recipe.ingredients.select_for_update().all()
        with transaction.atomic():
            for ingredient in ingredients:
                ingredient.product.usage_count += 1
                ingredient.product.save()
