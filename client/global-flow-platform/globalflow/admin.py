from django.contrib import admin
from .models import TodoItem, Sale

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Sale)
