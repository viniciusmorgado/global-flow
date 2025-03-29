from django.urls import path
from . import views

app_name = 'globalflow'

urlpatterns = [
    path("", views.index, name="index"),
    # path("todos/", views.todos, name="Todos"),
    
    path('business/', views.business, name='business'),
    path('exchange-process/', views.exchange, name='exchange_process'),
    path('broker/', views.broker, name='broker'),
    path('cargo/', views.cargo, name='cargo'),
    path('tax-regime/', views.tax_regime, name='tax_regime'),
    path('broker-type/', views.broker_type, name='broker_type'),
    path('radar/', views.radar, name='radar'),
    path('insurance/', views.insurance, name='insurance'), 
]
