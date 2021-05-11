from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    direccion = models.CharField(max_length=128)
    nombre = models.CharField(max_length=64)
    telefono = models.IntegerField(blank=True, null=True)
    cpp = models.IntegerField(blank=True, null=True)

class Item(models.Model): 
    CATEGORY_CHOICES = [ #Tuple not necesary. C ould change for list
    ('SP', 'Sports'),
    ('CU', 'Cubrebocas'),
    ('SC', 'Scrunchies'),
    ('BA', 'Trajes de Baño'),
    ('CA', 'Casual'),
    ]
    SEX_CHOICES = [ #Tuple not necesary. C ould change for list
    ('EL', 'Hombre'),
    ('ELLA', 'Mujer'),
    ]
    nombre= models.CharField(max_length=64)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=64, choices=CATEGORY_CHOICES)
    pic0 = models.CharField(max_length=256)
    sexo = models.CharField(max_length=64, choices = SEX_CHOICES, blank=True)
    n_pics = models.IntegerField()
    pic1 = models.CharField(max_length=256, blank=True)
    pic2 = models.CharField(max_length=256, blank=True)
    pic3 = models.CharField(max_length=256, blank=True)
    pic4 = models.CharField(max_length=256, blank=True)

class Carrito(models.Model): 
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_watched")    
    cantidad = models.IntegerField()
    talla = models.CharField(max_length=64, blank=True)
    color = models.CharField(max_length=64, blank=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE, related_name="watcher")

class Pedido(models.Model): 
    ESTATUS_CHOICES = [ #Tuple not necesary. C ould change for list
    ('PE', 'Pedido'),
    ('VE', 'Verificando Pago'),
    ('PR', 'En processo'),
    ('EN', 'Enviado'),
    ('RE', 'Recibido'),
    ]
    user= models.ForeignKey(User,on_delete=models.CASCADE, related_name="buyer")
    estatus = models.CharField(max_length=16, choices=ESTATUS_CHOICES)
    fecha = models.DateTimeField(blank=True)
    folio = models.IntegerField(blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item_bougth")    
    cantidad = models.IntegerField()
    talla = models.CharField(max_length=64, blank=True)
    color = models.CharField(max_length=64, blank=True)
    identifier = models.IntegerField(blank=True)