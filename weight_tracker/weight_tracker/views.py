from django.shortcuts import render, redirect
from .forms import WeightEntryForm
from .models import WeightEntry

import plotly.express as px

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

def plot_timeseries(request, username):
    entries = WeightEntry.objects.filter(username=username).order_by('date')

    dates = [entry.date for entry in entries]
    weights = [float(entry.weight_kg) for entry in entries]

    fig = px.line(
        x=dates,
        y=weights,
        labels={'x': 'Date', 'y': 'Weight (kg)'},
        title=f'Time Series Plot for {username}',
        markers=True,
    )

    plot_html = fig.to_html(full_html=False)

    return render(request, 'plot_timeseries.html', {'plot_html': plot_html})

