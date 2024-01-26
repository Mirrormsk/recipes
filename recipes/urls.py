from django.urls import path
from recipes import views
from recipes.apps import RecipesConfig

app_name = RecipesConfig.name


urlpatterns = [
    path("add_product_to_recipe/", views.add_product_to_recipe, name="add_product_to_recipe"),
]
