from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Productos

#ProductosCeramica, ProductosAcuarela, ProductosAbstractos

def lista_productos(request):
    return render(request, 'productos.html', {'productos': Productos.objects.all()})
  
def flitro_productos(request):
    tipo = request.GET.get('tipo')
    if tipo:
        productos = Productos.objects.filter(tipo=tipo)
    else:
        productos = Productos.objects.all()
    paginator = Paginator(productos, 15)  # 15 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'productos.html', {
        'productos': page_obj,
        'tipo': tipo,
        'page_obj': page_obj,
    })

def producto_individual(request, pk):
    producto = get_object_or_404(Productos, pk=pk)
    return render(request, 'productoindividual.html', {'producto': producto})

#def lista_acuarela(request):
 #   productos = ProductosAcuarela.objects.all()
  #  return render(request, 'productos/acuarela.html', {'productos': productos})

#def lista_abstractos(request):
 #   productos = ProductosAbstractos.objects.all()
  #  return render(request, 'productos/abstractos.html', {'productos': productos})
