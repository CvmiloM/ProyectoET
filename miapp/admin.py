from django.contrib import admin

# miapp/admin.py
from django.contrib import admin
from .models import UsuarioAdmin, Producto, Compra, DetalleCompra

admin.site.register(UsuarioAdmin)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(DetalleCompra)
