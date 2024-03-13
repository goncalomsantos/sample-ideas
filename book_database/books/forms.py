from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "author", "book_cover", "price"]

class StatusChangeForm(forms.Form):
    new_status = forms.ChoiceField(choices=[('have', 'Have'), ('want', 'Want')])