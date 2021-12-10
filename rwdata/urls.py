
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from rwdata import views

urlpatterns = [
    path('simple_upload/',views.simple_upload, name="simple_upload"),
    path('', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
]
