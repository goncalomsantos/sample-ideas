from django import forms
from .models import WeightEntry

class WeightEntryForm(forms.ModelForm):
    class Meta:
        model = WeightEntry
        fields = ['username', 'date', 'weight_kg']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
