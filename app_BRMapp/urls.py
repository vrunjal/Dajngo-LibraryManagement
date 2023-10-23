from django.contrib import admin
from django.urls import path
from app_BRMapp import views

urlpatterns = [
    path('view-books/',views.viewBook),
]