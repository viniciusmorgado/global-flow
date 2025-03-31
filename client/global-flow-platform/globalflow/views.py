from django.shortcuts import render, redirect
from globalflow.models import TodoItem, Sale, Dispatcher
from .utils import get_plot, get_pie_chart, get_bar_chart, get_scatter_plot
import random
import numpy as np
from datetime import datetime

def index(request):
    qs = Sale.objects.all()
    
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart1 = get_plot(x, y)
    
    labels = x[:5]
    sizes = y[:5]
    chart2 = get_pie_chart(labels, sizes)
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    monthly_sales = [random.randint(5000, 20000) for _ in range(6)]
    chart3 = get_bar_chart(months, monthly_sales)

    products = x[:8]
    prices = [random.uniform(10, 100) for _ in range(len(products))]
    chart4 = get_scatter_plot(products, prices)

    chart5 = get_bar_chart(months, monthly_sales)    
    chart6 = get_scatter_plot(products, prices)
    
    context = {
        "chart1": chart1,
        "chart2": chart2,
        "chart3": chart3,
        "chart4": chart4,
        "chart5": chart5,
        "chart6": chart6,
    }
    
    return render(request, "index.html", context)

def business(request):
    context = {}
    return render(request, 'business.html', context)

def exchange_process(request):
    context = {}
    return render(request, 'exchange_process.html', context)

def dispatcher(request):
    if request.method == 'GET':
        query = Dispatcher.objects.all()

    if request.method == 'POST':
        dispatcher_name = request.POST.get('dispatcher_name', '').strip()
        # if dispatcher_name:
        Dispatcher.objects.create(name=dispatcher_name)
        return redirect('globalflow:dispatcher')
        
    context = {
        'dispatchers': query 
    }

    return render(request, 'dispatcher.html', context)

def role(request):
    context = {}
    return render(request, 'role.html', context)

def tax_regime(request):
    context = {}
    return render(request, 'tax_regime.html', context)

def broker_type(request):
    context = {}
    return render(request, 'broker_type.html', context)

def radar(request):
    context = {}
    return render(request, 'radar.html', context)

def insurance(request):
    context = {}
    return render(request, 'insurance.html', context)
