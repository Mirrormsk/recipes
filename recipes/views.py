from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from recipes.models import Recipe, Product, Ingredient
from recipes.services import RecipeService


class RecipeListView(ListView):
    """
    List all recipes if param "exclude" not sent,
    else only recipes without exclude ingredient or if
    that ingredient count less than 10 g.
    """
    model = Recipe

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        excluded_product_id = self.request.GET.get('exclude')
        if excluded_product_id is not None:
            excluded_product = get_object_or_404(Product, id=excluded_product_id)
            context_data['excluded_product_name'] = excluded_product.title
        return context_data

    def get_queryset(self):
        excluded_product_id = self.request.GET.get('product_id')
        queryset = super().get_queryset()

        if excluded_product_id is not None:

            excluded_product = get_object_or_404(Product, id=excluded_product_id)
            recipes_with_excluded_product = queryset.filter(ingredients__product=excluded_product, ingredients__quantity__gt=10)
            return queryset.exclude(id__in=recipes_with_excluded_product)

        return queryset


def add_product_to_recipe(request):
    """Функция добавляет к указанному рецепту указанный
    продукт с указанным весом.
    Если в рецепте уже есть такой продукт, то функция
    должна поменять его вес в этом рецепте на указанный."""
    recipe_id = request.GET.get("recipe_id")
    product_id = request.GET.get("product_id")
    weight = request.GET.get("weight")

    if not all(map(bool, [recipe_id, product_id, weight])):
        return JsonResponse(
            {
                "message": "Missing one of required parameters (recipe_id, product_id, weight)"
            },
            status=400,
        )

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)
    ingredient, created = Ingredient.objects.update_or_create(
        recipe=recipe, product=product, quantity=weight
    )

    if created:
        message = f"Product '{product.title}' was successfully added to recipe {recipe.title}."
    else:
        message = (
            f"Product '{product.title}' was be corrected in recipe {recipe.title}."
        )

    return JsonResponse({"message": message}, status=201)


def cook_recipe(request):
    """Функция увеличивает на единицу количество
    приготовленных блюд для каждого продукта,
    входящего в указанный рецепт."""
    recipe_id = request.GET.get("recipe_id")
    if not recipe_id:
        return JsonResponse(
            {
                "message": "Missing one of required parameters recipe_id"
            },
            status=400,
        )

    recipe = get_object_or_404(Recipe, id=recipe_id)
    RecipeService.increment_ingredients_usage_counters(recipe)

    return JsonResponse({"message": "OK", "status": 200})


