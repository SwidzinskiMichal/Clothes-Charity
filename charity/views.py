from . import models
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def landingpage(request):
    return render(request, "charity/index.html", {'donations_all': models.Donation.objects.all().count(),
                                                  'organisations_all': models.Donation.objects.values('institution').distinct().count(),
                                                  'institutions': models.Institution.objects.all(),
                                                  'categories': models.Category.objects.all(),
                                                  'institution_categories': models.Institution.categories.through.objects.all()})


@login_required(login_url='/login/')
def donation(request):
    return render(request, "charity/form.html", {'categories': models.Category.objects.all()})


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/register/')
    else:
        return render(request, "charity/login.html")


def logout_user(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Create new user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name,
            last_name=surname
        )

        # Redirect to login page
        return redirect('/login/')
    else:
        return render(request, 'charity/register.html')
