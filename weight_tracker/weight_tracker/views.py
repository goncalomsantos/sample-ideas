from django.shortcuts import render, redirect
from .forms import WeightEntryForm
from .models import WeightEntry

def weight_entry(request):
    if request.method == 'POST':
        form = WeightEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('weight_entry')
    else:
        form = WeightEntryForm()

    entries = WeightEntry.objects.all()

    return render(request, 'weight_entry.html', {'form': form, 'entries': entries})
