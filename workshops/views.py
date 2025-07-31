from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import WorkshopPresupuestoForm
from .models import Workshop

def catalogo_workshops(request):
    workshops = Workshop.objects.all()
    return render(request, 'catalogo.html', {'workshops': workshops})

def detalle_workshop(request, workshop_id):
    try:
        workshop = Workshop.objects.get(id=workshop_id)
    except Workshop.DoesNotExist:
        return render(request, '404.html', status=404)

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

            # Preparar y enviar el mail
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

            send_mail(
                subject,
                message,
                {email},
                ['lauramartinez.ro@hotmail.com'],
            )

            return redirect('gracias')  # página de éxito
    else:
        form = WorkshopPresupuestoForm()

    return render(request, 'presupuesto.html', {'form': form})


def pagina_gracias(request):
    return render(request, 'gracias.html')

