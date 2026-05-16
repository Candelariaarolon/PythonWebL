from django.urls import path
from productos.views import lista_productos, flitro_productos, producto_individual, agregar_al_carrito, agregar_al_carrito_desde_lista, productos_presupuesto, agregar_personalizado

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('productos/filtrar/', flitro_productos, name='filtrar_productos'),
    path('producto/<int:pk>/', producto_individual, name='producto_individual'),
    path('agregar-al-carrito/', agregar_al_carrito, name='agregar_al_carrito'),
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito_desde_lista, name='agregar_al_carrito_desde_lista'),
    path('agregar-personalizado/', agregar_personalizado, name='agregar_personalizado'),
    path('presupuesto/', productos_presupuesto, name='productos_presupuesto'),
]

