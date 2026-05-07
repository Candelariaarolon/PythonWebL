# pago/views.py
from urllib.parse import quote
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from productos.models import Producto

WHATSAPP_NUMBER = '5493515101874'


def carrito(request):
    carrito = request.session.get('carrito', {})
    productos = Producto.objects.filter(id__in=carrito.keys())

    carrito_detalle = []
    for producto in productos:
        cantidad = carrito.get(str(producto.id), 0)
        subtotal = producto.precio_final * cantidad
        carrito_detalle.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
        })

    total = sum(item['subtotal'] for item in carrito_detalle)

    return render(request, 'carrito.html', {
        'carrito': carrito_detalle,
        'total': total,
    })


@require_POST
def quitar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    carrito.pop(str(producto_id), None)
    request.session['carrito'] = carrito
    return redirect('carrito')


@require_POST
def actualizar_cantidad(request):
    producto_id = request.POST.get('producto_id')
    try:
        cantidad = int(request.POST.get('cantidad', 1))
    except ValueError:
        cantidad = 1

    carrito = request.session.get('carrito', {})

    if cantidad <= 0:
        carrito.pop(str(producto_id), None)
    else:
        carrito[str(producto_id)] = cantidad

    request.session['carrito'] = carrito
    return redirect('carrito')


@require_POST
def realizar_pedido(request):
    carrito_session = request.session.get('carrito', {})
    if not carrito_session:
        return redirect('carrito')

    productos = Producto.objects.filter(id__in=carrito_session.keys())

    lineas = ['Hola Laura! Quiero realizar el siguiente pedido:', '']
    total = 0
    for producto in productos:
        cantidad = carrito_session.get(str(producto.id), 1)
        subtotal = producto.precio_final * int(cantidad)
        total += subtotal
        lineas.append(f'- {producto.Titulo} x{cantidad} — ${subtotal}')

    lineas.append('')
    lineas.append(f'Total: ${total}')

    mensaje = '\n'.join(lineas)
    url = f'https://wa.me/{WHATSAPP_NUMBER}?text={quote(mensaje)}'
    return redirect(url)
