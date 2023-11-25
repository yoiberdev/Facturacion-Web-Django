from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('factura/<int:id>', views.factura, name="factura"),   
    path('ventas/', views.ventas, name="ventas"),
]
