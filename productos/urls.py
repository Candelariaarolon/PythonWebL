from django.urls import path
from productos.views import lista_productos, flitro_productos, producto_individual

urlpatterns = [
    #path('ceramica/', views.lista_ceramica, name='lista_ceramica'),
    #path('acuarela/', views.lista_acuarela, name='lista_acuarela'),
    #path('abstractos/', views.lista_abstractos, name='lista_abstractos'),
    path('', lista_productos, name='lista_productos'),
    path('productos/filtrar/', flitro_productos, name='filtrar_productos'),
    path('producto/<int:pk>/', producto_individual, name='producto_individual'), 
]

