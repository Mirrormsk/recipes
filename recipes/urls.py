from django.urls import path
from recipes import views
from recipes.apps import RecipesConfig

app_name = RecipesConfig.name


urlpatterns = [
    path("add_product_to_recipe/", views.add_product_to_recipe, name="add_product_to_recipe"),
    path("cook_recipe/", views.cook_recipe, name="cook_recipe"),
    path("show_recipes_without_product", views.RecipeListView.as_view(), name="show_recipes_without_product"),
    path("", views.RecipeListView.as_view(), name="show_recipes_without_product")
]
