# pago/views.py
from urllib.parse import quote
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from productos.models import Producto

WHATSAPP_NUMBER = '5493515101874'


def _parsear_clave(clave):
    if '|' in clave:
        producto_id, diseño = clave.split('|', 1)
        return producto_id, diseño
    return clave, ''


def carrito(request):
    carrito_session = request.session.get('carrito', {})

    carrito_detalle = []
    for clave, cantidad in carrito_session.items():
        producto_id, diseño = _parsear_clave(clave)
        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            continue
        subtotal = producto.precio_final * cantidad
        carrito_detalle.append({
            'clave': clave,
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
            'diseño': diseño,
        })

    total = sum(item['subtotal'] for item in carrito_detalle)
    return render(request, 'carrito.html', {'carrito': carrito_detalle, 'total': total})


@require_POST
def quitar_del_carrito(request, producto_id=None):
    clave = request.POST.get('clave') or str(producto_id)
    carrito = request.session.get('carrito', {})
    carrito.pop(clave, None)
    request.session['carrito'] = carrito
    return redirect('carrito')


@require_POST
def actualizar_cantidad(request):
    clave = request.POST.get('clave') or request.POST.get('producto_id', '')
    try:
        cantidad = int(request.POST.get('cantidad', 1))
    except ValueError:
        cantidad = 1

    carrito = request.session.get('carrito', {})
    if cantidad <= 0:
        carrito.pop(clave, None)
    else:
        carrito[clave] = cantidad

    request.session['carrito'] = carrito
    return redirect('carrito')


@require_POST
def realizar_pedido(request):
    carrito_session = request.session.get('carrito', {})
    if not carrito_session:
        return redirect('carrito')

    lineas = ['Hola Laura! Quiero realizar el siguiente pedido:', '']
    total = 0
    for clave, cantidad in carrito_session.items():
        producto_id, diseño = _parsear_clave(clave)
        try:
            producto = Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            continue
        subtotal = producto.precio_final * int(cantidad)
        total += subtotal
        diseño_text = f' | Diseño: {diseño}' if diseño else ''
        lineas.append(f'- {producto.Titulo} (Pieza #{producto_id}) x{cantidad}{diseño_text} — ${subtotal}')

    lineas.append('')
    lineas.append(f'Total: ${total}')

    mensaje = '\n'.join(lineas)
    url = f'https://wa.me/{WHATSAPP_NUMBER}?text={quote(mensaje)}'
    return redirect(url)
