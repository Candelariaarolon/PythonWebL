from django.shortcuts import render

def inicio(request):
    
    return render(request, 'inicio.html', {})
    
   # template = loader.get_template('inicio.html')
   # template_renderizado = template.render({})
   # return HttpResponse(template_renderizado)
   

