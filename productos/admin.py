from django.contrib import admin

from .models import Producto, ProductoImagen

class ProductoImagenInline(admin.TabularInline):
    model = ProductoImagen
    extra = 1

class ProductosAdmin(admin.ModelAdmin):
    inlines = [ProductoImagenInline]

admin.site.register(Producto, ProductosAdmin)
admin.site.register(ProductoImagen)