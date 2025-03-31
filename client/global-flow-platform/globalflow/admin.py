from django.contrib import admin
from .models import TodoItem, Sale, BusinessRole, TaxRegime, Honorary, MinimumFee, SampleFee, Dispatcher, Insurance, Radar, Business

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Sale)
admin.site.register(BusinessRole)
admin.site.register(TaxRegime)
admin.site.register(Honorary)
admin.site.register(MinimumFee)
admin.site.register(SampleFee)
admin.site.register(Dispatcher)
admin.site.register(Insurance)
admin.site.register(Radar)
admin.site.register(Business)
