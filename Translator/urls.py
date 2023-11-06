from django.contrib import admin
from django.urls import path
from TranslatorApp import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('',views.signup, name="signup")
    # Other URL patterns for your app
]
