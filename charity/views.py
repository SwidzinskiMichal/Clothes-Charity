from django.shortcuts import render


def landingpage(request):
    return render(request, "charity/index.html")


def donation(request):
    return render(request, "charity/form.html")


def login(request):
    return render(request, "charity/login.html")


def register(request):
    return render(request, "charity/register.html")
