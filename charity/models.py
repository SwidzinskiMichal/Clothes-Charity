from django.db import models
from django.contrib.auth.models import User


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


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=50)
    city = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=50)
    pick_up_date = models.DateField()
    pick_up_time = models.DateField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
