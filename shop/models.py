from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    telefono = models.CharField(max_length=12, blank=True, null=True)
    cpp = models.IntegerField(blank=True, null=True)
    calle = models.CharField(max_length=50,blank=True)
    N_interior = models.CharField(max_length=10,blank=True)
    N_exterior = models.CharField(max_length=10,blank=True)
    colonia = models.CharField(max_length=50,blank=True)
    municipio = models.CharField(max_length =20,blank=True)
    estado = models.CharField(max_length=20,blank=True) 
    ciudad = models.CharField(max_length=20,blank=True) 



class Item(models.Model): 
    CATEGORY_CHOICES = [ #Tuple not necesary. C ould change for list
    ('SP', 'Sports'),
    ('CU', 'Cubrebocas'),
    ('SC', 'Scrunchies'),
    ('BA', 'Trajes de Baño'),
    ('CA', 'Mandiles'),
    ('TW', 'Twerk')
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
    color_disp = models.CharField(max_length=256, blank = True) 
    soldout = models.IntegerField(blank=True, default=0)

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
    envio = models.CharField(blank = True, max_length=50)