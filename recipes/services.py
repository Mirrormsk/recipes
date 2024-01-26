from recipes.models import Recipe


class RecipeService:

    @staticmethod
    def increment_ingredients_usage_counters(recipe: Recipe):
        """Increments the recipe ingredients usage counters

        :param recipe: Recipe instance
        :type recipe: Recipe
        :return: None
        """
        for ingredient in recipe.ingredients.all():
            ingredient.product.usage_count += 1
            ingredient.product.save()

