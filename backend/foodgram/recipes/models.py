from django.db import models

class Tags(models.Model):

    name = models.CharField(max_length=200,
                            verbose_name='название',
                            unique=True)
    color = models.CharField(max_length=7,
                             verbose_name='цвет (HEX)',
                             unique=True)
    slug = models.SlugField(verbose_name='slug',
                            unique=True,
                            max_length=200)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredients(models.Model):

    name = models.CharField(
        'Ингредиент',
        max_length=200)
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=200)

    class Meta:
        verbose_name = ("Ингредиент")
        verbose_name_plural = ("Ингредиенты")

    def __str__(self):
        return self.name
