from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from .models import Producto, ProductoImagen


class ProductoImagenInline(TabularInline):
    model = ProductoImagen
    extra = 1
    fields = ["imagen"]


@admin.register(Producto)
class ProductoAdmin(ModelAdmin):
    list_display = [
        "miniatura",
        "Titulo",
        "tipo",
        "Precio",
        "descuento",
        "precio_final",
        "stock",
        "destacado",
    ]
    list_editable = ["Precio", "descuento", "stock", "destacado"]
    list_filter = ["tipo", "destacado"]
    search_fields = ["Titulo", "Diseño", "Descripcion"]
    list_per_page = 20

    fieldsets = [
        ("Producto", {
            "fields": ["Titulo", "tipo", "Diseño", "Descripcion", "foto"],
        }),
        ("Precio y stock", {
            "fields": ["Precio", "descuento", "stock"],
        }),
        ("Visibilidad", {
            "fields": ["destacado"],
        }),
        ("Tamaño", {
            "fields": ["Tamaño"],
        }),
    ]

    inlines = [ProductoImagenInline]

    def miniatura(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" style="width:50px; height:50px; object-fit:cover; border-radius:6px;" />',
                obj.foto.url,
            )
        return "—"
    miniatura.short_description = "Foto"

    def precio_final(self, obj):
        return f"${obj.precio_final}"
    precio_final.short_description = "Precio final"