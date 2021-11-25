from django.db import models


class Category(models.Model):
    name = models.CharField("Název", max_length=30, unique=True)
