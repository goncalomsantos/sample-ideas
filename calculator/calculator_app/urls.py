# calculator_app/urls.py

from django.urls import path
from .views import calculator, calculate

urlpatterns = [
    path('', calculator, name='calculator'),   # URL for the main calculator view
    path('calculate/', calculate, name='calculate'),  # URL for the calculation view
]
