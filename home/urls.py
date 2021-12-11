from django.contrib import admin
from django.urls import path
from home import views
import home

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('resetpassword', views.resetpassword, name='resetpassword'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('createpage', views.create, name='create')
    
]
