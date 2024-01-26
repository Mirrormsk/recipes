from django.contrib import admin
from recipes.models import Recipe, Product, Ingredient


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'usage_count']
    fields = ['title', 'usage_count']
    readonly_fields = ['usage_count']
    search_fields = ['title']
    ordering = ['-usage_count']


class IngredientInlineAdmin(admin.TabularInline):
    model = Ingredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    fields = ['title']
    inlines = [IngredientInlineAdmin]
    search_fields = ['title']
    ordering = ['-pk']

