from . import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import EditProfileForm
from .models import Donation


def landingpage(request):
    return render(request, "charity/index.html", {'donations_all': models.Donation.objects.all().count(),
                                                  'organisations_all': models.Donation.objects.values('institution').distinct().count(),
                                                  'institutions': models.Institution.objects.all(),
                                                  'categories': models.Category.objects.all(),
                                                  'institution_categories': models.Institution.categories.through.objects.all()})


@login_required(login_url='/login/')
def donation(request):
    return render(request, "charity/form.html", {'categories': models.Category.objects.all(),
                                                 'institutions': models.Institution.objects.all(),
                                                 'institution_categories': models.Institution.categories.through.objects.all(),})


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


def user_profile(request):
    return render(request, 'charity/user_profile.html', {'user': request.user,
                                                         'donations':models.Donation.objects.all(),})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if user.check_password(password):
                user.save()
                return redirect('/profile/')
            else:
                form.add_error('password', 'Incorrect password')
    else:
        form = EditProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })
    context = {'form': form}
    return render(request, 'charity/edit_profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/profile/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'charity/change_password.html', {'form': form})


def take_donation(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)

    if request.method == 'POST':
        donation.is_taken = True
        donation.save()
        return redirect('/profile/')


def return_donation(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)

    if request.method == 'POST':
        donation.is_taken = False
        donation.save()
        return redirect('/profile/')


