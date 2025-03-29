from django.shortcuts import render
from globalflow.models import TodoItem, Sale
from .utils import get_plot

def index(request):
    qs = Sale.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x, y)

    return render(request, "index.html", {"chart": chart})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def business(request):
    context = {}
    return render(request, 'business.html', context)

def radar(request):
    context = {}
    return render(request, 'radar.html', context)

def broker_type(request):
    context = {}
    return render(request, 'broker_type.html', context)

def tax_regime(request):
    context = {}
    return render(request, 'tax_regime.html', context)

def cargo(request):
    context = {}
    return render(request, 'cargo.html', context)

def broker(request):
    context = {}
    return render(request, 'broker.html', context)

def exchange(request):
    context = {}
    return render(request, 'exchange.html', context)

def insurance(request):
    context = {}
    return render(request, 'insurance.html', context)
