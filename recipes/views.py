from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from recipes.models import Recipe, Product, Ingredient


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
