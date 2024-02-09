from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.db import models

from .forms import WeightEntryForm
from .models import WeightEntry

import plotly.express as px
import plotly.graph_objects as go

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

def top_usernames(request):
    top_usernames = WeightEntry.objects.values('username').annotate(
        weight_difference=models.Max('weight_kg') - models.Min('weight_kg')
    ).order_by('-weight_difference')[0:10]

    # Create a Plotly line chart for the top usernames
    fig = go.Figure()

    for username in top_usernames:
        # Retrieve the weight entries for each top username
        entries = WeightEntry.objects.filter(username=username['username']).order_by('date')

        # Extract data for Plotly
        dates = [entry.date for entry in entries]
        weights = [float(entry.weight_kg) for entry in entries]

        # Add a line to the chart for each top username
        fig.add_trace(go.Scatter(x=dates, y=weights, name=username['username']))

    # Set chart layout and title
    fig.update_layout(title='Top 10 Usernames - Weight Over Time', xaxis_title='Date', yaxis_title='Weight (kg)')

    # Convert the plot to HTML
    plot_html = fig.to_html(full_html=False)

    return render(request, 'top_10_timeseries.html', {'plot_html': plot_html})

