from django.urls import path
from . import views

app_name = 'globalflow'

urlpatterns = [
    path("", views.index, name="index"),
    path('business/', views.business, name='business'),
    path('exchange-process/', views.exchange_process, name='exchange_process'),
    path('dispatcher/', views.dispatcher, name='dispatcher'),
    path('role/', views.role, name='role'),
    path('tax-regime/', views.tax_regime, name='tax_regime'),
    path('broker-type/', views.broker_type, name='broker_type'),
    path('radar/', views.radar, name='radar'),
    path('insurance/', views.insurance, name='insurance') 
]
