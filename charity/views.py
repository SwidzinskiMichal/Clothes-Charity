from django.shortcuts import render
from . import models

def landingpage(request):
    return render(request, "charity/index.html", {'donations_all': models.Donation.objects.all().count(),
                                                  'organisations_all': models.Donation.objects.values('institution').distinct().count()})


def donation(request):
    return render(request, "charity/form.html")


def login(request):
    return render(request, "charity/login.html")


def register(request):
    return render(request, "charity/register.html")
