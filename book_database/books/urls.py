# books/urls.py
from django.urls import path
from .views import add_book, book_details, change_status

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path("book_details/<slug:slug>/", book_details, name="book_details"),
    path('books/<slug:slug>/change_status/', change_status, name='change_status'),
]
