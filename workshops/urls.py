from django.urls import path
from . import views

urlpatterns = [
    path('workshops/', views.catalogo_workshops, name='catalogo_workshops'),
    path('workshops/detalles/<int:pk>', views.detalle_workshop, name='detalle_workshop'),
    path('workshops/presupuesto/', views.pedir_presupuesto, name='pedir_presupuesto'),
    path('workshops/gracias/', views.pagina_gracias, name='gracias'),
]