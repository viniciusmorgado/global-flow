from django.shortcuts import render
from globalflow.models import TodoItem, Sale
from .utils import get_plot

def index(request):
    qs = Sale.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x, y)

    return render(request, "index.html", {"chart": chart})

def business(request):
    context = {}
    return render(request, 'business.html', context)

def exchange_process(request):
    context = {}
    return render(request, 'exchange_process.html', context)

def dispatcher(request):
    context = {}
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
