
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include("gradesign.urls")),#登录页面urls
]
