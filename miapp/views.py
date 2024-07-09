from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Compra, DetalleCompra, UsuarioAdmin
from .forms import ProductoForm, UsuarioAdminForm
from django.http import JsonResponse
import json
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import FormUsuario
from .models import UsuarioAdmin




from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    decorated_view = user_passes_test(
        lambda user: user.is_staff,
        login_url='/login/'
    )(view_func)
    return decorated_view

@login_required
def lista_compra(request):
    compras = Compra.objects.all()
    return render(request, 'lista_compra.html', {'compras': compras})

@login_required
def detalle_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    detalles = DetalleCompra.objects.filter(compra=compra)
    return render(request, 'detalle_compra.html', {'compra': compra, 'detalles': detalles})

# Vistas para Producto

@login_required
@admin_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


@login_required
@admin_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'form_producto.html', {'form': form})



@login_required
@admin_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'form_producto.html', {'form': form})


@login_required
@admin_required
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'confirmar_eliminar.html', {'producto': producto})

# Vistas para UsuarioAdmin


@login_required
@admin_required
def crear_usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('lista_usuarios')
    else:
        form = FormUsuario()
    return render(request, 'form_usuario.html', {'form': form})


@login_required
@admin_required
def lista_usuarios(request):
    usuarios = UsuarioAdmin.objects.all()  # Aquí utilizamos UsuarioAdmin.objects en lugar de User.objects
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def guardar_carrito(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            carrito = data.get('carrito', [])
            
            if carrito:
                compra = Compra.objects.create(usuario=request.user)
                for item in carrito:
                    try:
                        producto = Producto.objects.get(id=item['id'])
                        cantidad = item['cantidad']
                        DetalleCompra.objects.create(compra=compra, producto=producto, cantidad=cantidad)
                    except Producto.DoesNotExist:
                        return JsonResponse({'success': False, 'error': f'Producto con ID {item["id"]} no existe.'})
                
                # Enviar correo
                asunto = 'Confirmación de compra'
                mensaje = f'Has realizado una compra con el ID {compra.id}.\n\nDetalles de la compra:\n'
                for item in carrito:
                    mensaje += f"- {item['nombre']} x {item['cantidad']} - ${item['precio'] * item['cantidad']}\n"
                try:
                    send_mail(asunto, mensaje, 'venta.de.productos.1.321@gmail.com', ['camilomongelara@gmail.com'])
                except Exception as e:
                    return JsonResponse({'success': False, 'error': f'Error al enviar el correo: {str(e)}'})

                return JsonResponse({'success': True, 'compra_id': compra.id})
            else:
                return JsonResponse({'success': False, 'error': 'El carrito está vacío.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido.'})

# Vistas para Compras
@login_required
def lista_compras(request):
    compras = Compra.objects.all()
    return render(request, 'lista_compras.html', {'compras': compras})

@login_required
def detalle_compra(request, compra_id):
    compra = Compra.objects.get(id=compra_id)
    detalles = DetalleCompra.objects.filter(compra=compra)
    return render(request, 'detalle_compra.html', {'compra': compra, 'detalles': detalles})

# Vista del index
def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

@login_required
def ver_carrito(request):
    return render(request, 'carrito.html')

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def lista_usuarios(request):
    usuarios = UsuarioAdmin.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(UsuarioAdmin, id=usuario_id)
    if usuario.username == 'admin':
        return redirect('lista_usuarios')  # Redirigir sin eliminar si el usuario es admin
    usuario.delete()
    return redirect('lista_usuarios')
