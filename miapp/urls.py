# en urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import lista_usuarios, eliminar_usuario
from django.conf.urls.static import static
from miapp.views import (
    lista_productos, crear_producto, editar_producto, eliminar_producto, 
    lista_usuarios, crear_usuario, guardar_carrito, 
    lista_compras, detalle_compra, index, ver_carrito, CustomLoginView, CustomLogoutView
)

urlpatterns = [
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('usuarios/crear/', crear_usuario, name='crear_usuario'),
    path('guardar_carrito/', guardar_carrito, name='guardar_carrito'),
    path('compras/', lista_compras, name='lista_compras'),
    path('compras/<int:compra_id>/', detalle_compra, name='detalle_compra'),
    path('', index, name='index'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('usuarios/eliminar/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
