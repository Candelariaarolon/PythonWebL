# pago/views.py
from django.shortcuts import render
from productos.models import Producto   # <-- importamos el modelo real
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
                       
def carrito(request):
    carrito = request.session.get('carrito', {})           # {'1': 2, '5': 1, ...}
    productos = Producto.objects.filter(id__in=carrito.keys())
    
    carrito_detalle = []
    for producto in productos:                             # <--- productos, no producto
        cantidad = carrito.get(str(producto.id), 0)
        subtotal = producto.Precio * cantidad
        carrito_detalle.append({
            'producto':   producto,
            'cantidad':   cantidad,
            'subtotal':   subtotal,
        })

    total = sum(item['subtotal'] for item in carrito_detalle)

    return render(request, 'carrito.html', {
        'carrito': carrito_detalle,
        'total':   total,
    })



@require_POST
def quitar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    # elimina si existe (no da error si no está)
    carrito.pop(str(producto_id), None)
    request.session['carrito'] = carrito
    return redirect('carrito')   # o 'pago:carrito' si usás namespace

@require_POST
def actualizar_cantidad(request):
    producto_id = request.POST.get('producto_id')
    try:
        cantidad = int(request.POST.get('cantidad', 1))
    except ValueError:
        cantidad = 1

    carrito = request.session.get('carrito', {})

    # si el usuario puso cantidad <= 0, podés decidir quitar el producto:
    if cantidad <= 0:
        carrito.pop(str(producto_id), None)
    else:
        carrito[str(producto_id)] = cantidad

    request.session['carrito'] = carrito
    # mejor redirect para aplicar Post/Redirect/Get y evitar reposts al recargar
    return redirect('carrito')   # o 'pago:carrito' si usás namespace