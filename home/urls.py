from django.contrib import admin
from django.urls import path

import home
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create", views.create, name="create"),
]
