from django.contrib import admin

from .models import Productos, ProductoImagen

class ProductoImagenInline(admin.TabularInline):
    model = ProductoImagen
    extra = 1

class ProductosAdmin(admin.ModelAdmin):
    inlines = [ProductoImagenInline]

admin.site.register(Productos, ProductosAdmin)
admin.site.register(ProductoImagen)