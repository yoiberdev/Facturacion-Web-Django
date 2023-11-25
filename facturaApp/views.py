from django.shortcuts import render
from .models import Cliente,Producto, Venta
from django.shortcuts import get_object_or_404, render, redirect
from .forms import createNewCliente

from django.http import JsonResponse
import json
from .utils import procesar_datos


# Create your views here.
def index(request):
    title= "Django Course!!!"
    if request.method == 'GET': 
        return render(request,'index.html', {
            'form1': createNewCliente(),
        })
    else:
        dni = request.POST['dni']
        mi_modelo = Cliente.objects.filter(dni = dni)
        check = mi_modelo.exists()
        contador = request.POST['contador']#Contador del input hidden


        #json
        #data = json.loads(request.POST.get('datos_json'))
        #data = json.loads(request.POST.get('datos_json'))
        #procesar_datos(data)



        if(check == True):
            cliente = get_object_or_404(Cliente, dni = dni)
            venta = Venta.objects.create(ruc=request.POST['ruc'], cliente_id= cliente.id)
            
            #Crear productos de acuerdo al contador enviado por el hidden
            for i in range(1,int(contador)+1):
                producto = Producto.objects.create(producto=request.POST.get('prodbtn{}'.format(i), ''), precio=request.POST.get('preciobtn{}'.format(i), 0), cantidad=request.POST.get('cantbtn{}'.format(i), 0), venta_id=venta.id)
            return redirect('ventas')
        else:
            cliente=Cliente.objects.create(cliente=request.POST['cliente'], direccion=request.POST['direccion'], dni=request.POST['dni'])
            venta = Venta.objects.create(ruc=request.POST['ruc'], cliente_id=cliente.id)
            for i in range(1,int(contador)+1):
                producto = Producto.objects.create(producto=request.POST.get('prodbtn{}'.format(i), ''), precio=request.POST.get('preciobtn{}'.format(i), 0), cantidad=request.POST.get('cantbtn{}'.format(i), 0), venta_id=venta.id)
            #producto = Producto.objects.create(producto=request.POST['producto'], precio=request.POST['precio'], cantidad=request.POST['cantidad'], venta_id=venta.id)
            return redirect('ventas')
   

def factura(request, id):
    venta= get_object_or_404(Venta, id=id)
    cliente= get_object_or_404(Cliente, id=venta.cliente_id)
    productos=Producto.objects.filter(venta_id = id)
    total=0
    subtotal=[]
    for i in productos:
        total+=i.precio*i.cantidad
        subtotal.append(i.precio*i.cantidad)
    return render(request, 'factura.html',{
        'cliente': cliente,
        'venta': venta,
        'productos': productos,
        'total': total,
        'subtotal': subtotal,
    })

def ventas(request):
    ventas = Venta.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'ventas.html',{
        'ventas': ventas,
        'clientes':clientes
    })
