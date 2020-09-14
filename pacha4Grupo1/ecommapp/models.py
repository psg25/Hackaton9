from django.db import models
from ecommprj import settings
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse

# Create your models here.

CATEGORIAS_OPCIONES = (
    ('FE', 'Front End'),
    ('BE', 'Back End'),
    ('UX', 'User Experience'),
    ('MD', 'Marketing Digital'),
    ('DV', 'Desarrollo de Videojuegos'),
    ('DM', 'Desarrollo de App para móviles'),
    ('DA', 'Data Analytics'),
    ('FA', 'Front End Avanzado'),

)

ETIQUETAS_OPCIONES = (
    ('01', 'Desarrollo Web'),
    ('02', 'Marketing Digital'),
    ('03', 'Diseno de Juegos'),
    ('04', 'Diseno de Apps'),

)

class Usuario(AbstractUser):
    cliente_id = models.CharField(max_length=100, blank=True, null=True)


class Programas(models.Model):
    curso = models.CharField(max_length=100)
    precio = models.FloatField()
    descuento_precio = models.FloatField(blank=True, null=True)
    categoria = models.CharField(choices=CATEGORIAS_OPCIONES, max_length=2)
    etiqueta = models.CharField(choices=ETIQUETAS_OPCIONES, max_length=1)
    slug = models.SlugField()
    descripcion = models.TextField()
    imagen = models.ImageField()

    def __str__(self):
        return self.curso

    def get_absolute_url(self):
        return reverse("programa", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("anadir-al-carrito", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("quitar-del-carrito", kwargs={
            'slug': self.slug
        })

class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pedido = models.BooleanField(default=False)
    curso = models.ForeignKey(Programas, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

class Pago(models.Model):
    pass

class Cupon(models.Model):
    pass

