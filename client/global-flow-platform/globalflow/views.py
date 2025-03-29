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
