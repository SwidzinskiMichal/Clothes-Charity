from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


choices = [('fundacja', 'Fundacja'),
           ('organizacja_pozarzadowa', 'Organizacja pozarządowa'),
           ('zbiorka_lokalna', 'Zbiórka lokalna')]


class Institution(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=30, choices=choices, default= 'fundacja')
    categories = models.ManyToManyField(Category)
