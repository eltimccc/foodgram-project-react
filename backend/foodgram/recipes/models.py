from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Tags(models.Model):
    """Модель Тегов."""

    name = models.CharField(max_length=200, verbose_name="название", unique=True)
    color = models.CharField(max_length=7, verbose_name="цвет (HEX)", unique=True)
    slug = models.SlugField(verbose_name="slug", unique=True, max_length=200)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Модель Ингредиентов."""

    name = models.CharField("Ингредиент", max_length=200)
    measurement_unit = models.CharField("Единица измерения", max_length=200)
    constraints = [
        models.UniqueConstraint(
            fields=["name", "measurement_unit"], name="unique_name_m_unit"
        )
    ]

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель Рецептов."""

    tags = models.ManyToManyField(
        Tags, related_name="recipes", verbose_name="Тег рецепта"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор рецепта"
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through="RecipeIngredient",
        verbose_name="Ингредиенты",
        related_name="recipes",
    )
    name = models.CharField(max_length=200, verbose_name="Название рецепта")
    image = models.ImageField(verbose_name="Фото рецепта")
    text = models.TextField(verbose_name="Описание рецепта")
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name="Время приготовления",
        default=1,
        validators=[MinValueValidator(1, message="Не может быть равно нулю")],
    )

    class Meta:
        ordering = ("-id",)
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class RecipeIngredient(models.Model):
    """Модель Рецептов + Ингредиентов."""

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ingredients_in_recipe"
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="ingredients_in_recipe",
        verbose_name="Ингредиент",
    )
    amount = models.SmallIntegerField(
        verbose_name="Кол-во ингредиентов",
        default=1,
        validators=[
            MinValueValidator(
                1,
                message="Не равно нулю или отрицательному числу",
            )
        ],
    )

    class Meta:
        verbose_name = "Ингредиент в рецепте"
        verbose_name_plural = "Ингредиенты в рецептах"
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "ingredient"],
                name="unique_ingredient",
            )
        ]

    def __str__(self):
        return (
            f"{self.ingredient.name}"
            f"{self.amount}"
            f"{self.ingredient.measurement_unit}"
        )


class Favorite(models.Model):
    """Модель для Избранного."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user"
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="favorite_recipe"
    )

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"], name="unique_user_recipe"
            )
        ]


class ShopList(models.Model):
    """Модель для Листа Покупок."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart_recipe"
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="cart_recipe"
    )

    class Meta:
        verbose_name = "Список покупок"
        verbose_name_plural = "Списки покупок"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"], name="unique_customer_recipe"
            )
        ]


class Follow(models.Model):
    """Модель для Подписок."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follower"
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "following"], name="unique_following"
            )
        ]
