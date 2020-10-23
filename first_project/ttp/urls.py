from django.contrib import admin
from django.urls import path, include
from .views import final
urlpatterns = [
    path('ttp/',final)

]