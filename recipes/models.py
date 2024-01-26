from django.db import models
from django.db.models import ManyToManyField


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    usage_count = models.PositiveIntegerField(default=0, verbose_name="Использован")

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = "рецепт"
        verbose_name_plural = "рецепты"

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="Продукт"
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="Рецепт")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    quantity_unit = models.CharField(
        max_length=10, verbose_name="Единица измерения", default="г."
    )

    class Meta:
        verbose_name = "ингредиент"
        verbose_name_plural = "ингредиенты"
        unique_together = ("product", "recipe")

    def __str__(self):
        return f"{self.product.title} - {self.quantity} {self.quantity_unit}"
