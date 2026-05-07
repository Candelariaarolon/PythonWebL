from django.shortcuts import render
from productos.models import Producto

def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'inicio.html', {'productos': productos})
    
   # template = loader.get_template('inicio.html')
   # template_renderizado = template.render({})
   # return HttpResponse(template_renderizado)
   

