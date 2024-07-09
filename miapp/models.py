from django.db import models

# miapp/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UsuarioAdminManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class UsuarioAdmin(AbstractUser):
    # Añade campos personalizados aquí si es necesario
    pass

    # Añadir los related_name únicos
    groups = models.ManyToManyField(
        Group,
        related_name='usuarioadmin_groups',  # related_name único
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                    'granted to each of their groups.'),
        related_query_name='usuarioadmin'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarioadmin_user_permissions',  # related_name único
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuarioadmin'
    )


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    stock = models.IntegerField(default=0)  # Agregar el campo stock

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    usuario = models.ForeignKey(UsuarioAdmin, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='DetalleCompra')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Compra #{self.id} - Usuario: {self.usuario.username}'

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'
