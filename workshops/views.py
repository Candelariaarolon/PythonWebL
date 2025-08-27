from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.http import urlencode
from .forms import WorkshopPresupuestoForm
from .models import Workshop
from django.core.paginator import Paginator

def catalogo_workshops(request):
    workshops = Workshop.objects.all()  # tu queryset
    paginator = Paginator(workshops, 6)  # 6 productos por página

    page_number = request.GET.get('page')  # número de página desde la URL
    page_obj = paginator.get_page(page_number)  # objeto paginado

    return render(request, 'catalogo_workshops.html', {'page_obj': page_obj})

def detalle_workshop(request, pk):
    workshop = Workshop.objects.get(id=pk)
    return render(request, 'detalle_workshop.html', {'workshop': workshop})

    
def pedir_presupuesto(request):
    if request.method == 'POST':
        form = WorkshopPresupuestoForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            cantidad = form.cleaned_data['cantidad']
            diseño = form.cleaned_data['diseño']
            catering = form.cleaned_data['catering']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']

            # ---- Envío del mail como ya lo tenías ----
            subject = "Nuevo pedido de presupuesto de workshop"
            message = f"""
            Pedido de presupuesto:

            Tipo de taller: {tipo}
            Cantidad de personas: {cantidad}
            Diseño: {diseño}
            ¿Catering?: {'Sí' if catering else 'No'}

            Datos del cliente:
            Email: {email}
            Teléfono: {telefono}
            """

      #      send_mail(
      #          subject,
     #           message,
       #         email,  # remitente
        #        ['lauramartinez.ro@hotmail.com'],
         #   )

            # ---- Generar mensaje para WhatsApp ----
            whatsapp_msg = f"""Hola, quiero pedir un presupuesto:
Tipo de taller: {tipo}
Cantidad de personas: {cantidad}
Diseño: {diseño}
Catering: {'Sí' if catering else 'No'}
Email: {email}
Teléfono: {telefono}"""

            params = urlencode({'text': whatsapp_msg})
            numero = "5493515101874"  # sin el "+"
            whatsapp_url = f"https://wa.me/{numero}?{params}"

            return redirect(whatsapp_url)  # redirige directo a WhatsApp

    else:
        form = WorkshopPresupuestoForm()

    return render(request, 'presupuesto.html', {'form': form})


def pagina_gracias(request):
    return render(request, 'gracias.html')

