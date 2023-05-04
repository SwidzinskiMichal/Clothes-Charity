from django.urls import path
from . import views

app_name = 'charity'

urlpatterns = [
    path('register/', views.register, name='registration'),
    path('login/', views.login_user, name='login'),
    path('', views.landingpage, name='landingpage'),
    path('donation/', views.donation, name='donation'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]
