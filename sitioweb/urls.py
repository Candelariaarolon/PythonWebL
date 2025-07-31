"""
URL configuration for sitioweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  #ya viene definido dentro del propio framework Django, en su módulo de administración
    path('', include('inicio.urls')),
    path('productos/', include('productos.urls')),
    path('workshops/', include('workshops.urls')),
    path('pago/', include('pago.urls')),

]

"""
sitioweb es el corazón de configuración del proyecto, no es una app funcional con rutas propias, por eso no aparece en urlpatterns como las otras apps.
Se encarga de incluir las rutas de otras apps.

"""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)