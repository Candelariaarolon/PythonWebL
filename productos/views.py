from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.views.decorators.http import require_POST
from django.utils.http import urlencode

#ProductosCeramica, ProductosAcuarela, ProductosAbstractos

def lista_productos(request):
    return render(request, 'productos.html', {'productos': Producto.objects.all()})
  
def flitro_productos(request):
    tipo = request.GET.get('tipo')
    if tipo:
        productos = Producto.objects.filter(tipo=tipo)
    else:
        productos = Producto.objects.all()
    paginator = Paginator(productos, 15)  # 15 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'productos.html', {
        'productos': page_obj,
        'tipo': tipo,
        'page_obj': page_obj,
    })

def producto_individual(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productoindividual.html', {'producto': producto})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.views.decorators.http import require_POST

@require_POST
def agregar_al_carrito(request):
    producto_id = request.POST.get('producto_id')
    cantidad = int(request.POST.get('cantidad', 1))
    producto = get_object_or_404(Producto, id=producto_id)

    carrito = request.session.get('carrito', {})

    if producto_id in carrito:
        carrito[producto_id] += cantidad
    else:
        carrito[producto_id] = cantidad

    request.session['carrito'] = carrito
    return redirect('carrito')  # Podés cambiar 'carrito' por el nombre de la vista que muestra el carrito


# Desde productos.html
def agregar_al_carrito_desde_lista(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})

    producto_id_str = str(producto_id)
    if producto_id_str in carrito:
        carrito[producto_id_str] += 1
    else:
        carrito[producto_id_str] = 1

    request.session['carrito'] = carrito
    return redirect('filtrar_productos')  # Redirige a la página de filtrado de productos



    
def productos_presupuesto(request):
    
    carrito = request.session.get('carrito', {})
    if not carrito:
        whatsapp_msg = "Pedido de productos:%0A(No hay productos en el carrito)"
    else:
        whatsapp_msg = "Pedido de productos:\n"
        total = 0
        for producto_id, cantidad in carrito.items():
            producto = Producto.objects.get(id=producto_id)
            subtotal = producto.Precio * cantidad
            whatsapp_msg += f"- {producto.Titulo} x{cantidad}: ${subtotal:.2f}\n"
            total += subtotal
        whatsapp_msg += f"\nTotal: ${total:.2f}"

    params = urlencode({'text': whatsapp_msg})
    numero = "5493515101874"
    whatsapp_url = f"https://wa.me/{numero}?{params}"
    return redirect(whatsapp_url)
