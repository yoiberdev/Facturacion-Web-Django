# utils.py

from django.shortcuts import get_object_or_404
from .models import Cliente, Venta, Producto

def procesar_datos(data):
    dni = data['dni']
    mi_modelo = Cliente.objects.filter(dni=dni)
    check = mi_modelo.exists()
    contador = data['contador']

    if check:
        cliente = get_object_or_404(Cliente, dni=dni)
        venta = Venta.objects.create(ruc=data['ruc'], cliente=cliente)
    else:
        cliente = Cliente.objects.create(cliente=data['cliente'], direccion=data['direccion'], dni=dni)
        venta = Venta.objects.create(ruc=data['ruc'], cliente=cliente)

    for i in range(1, int(contador) + 1):
        Producto.objects.create(
            producto=data['prodbtn' + str(i)],
            precio=data['preciobtn' + str(i)],
            cantidad=data['cantbtn' + str(i)],
            venta=venta
        )
