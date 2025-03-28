from django.shortcuts import render, HttpResponse

from globalflow.models import TodoItem

# Create your views here.
def index(request):
    # return HttpResponse("Hello, World")
    return render(request, "index.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
