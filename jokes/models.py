from django.db import models


class Category(models.Model):
    name = models.CharField("Název", max_length=150, unique=True)


class Joke(models.Model):
    content = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Kategorie")
