# This piece of code Populates the existing database
# I do this so I dont have to do it manually at admin site.

from shop.models import Item

a = Item(
    nombre = "Blusa sport", 
    precio = 350, 
    categoria = "SP", 
    pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport1.jpg", 
    sexo = "ELLA", 
    n_pics = 3,
    pic1 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport1_1.jpg",
    pic2 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport1_2.jpg", 
    pic3 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport1_3.jpg", 
    color_disp = "Azul,Caquis,Rosa",
    descripcion = "Buena para hacer ejercicio   "
)
a.save()

a = Item(
    nombre = "Producto 2", 
    precio = 350, 
    categoria = "SP", 
    pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport2.jpg", 
    sexo = "ELLA", 
    n_pics = 2,
    pic1 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport2_1.jpg",
    pic2 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport2_2.jpg", 
    color_disp = "Blanco Liso, Rojo pasion"
)
a.save()

a = Item(
    nombre = "Producto 3", 
    precio = 350, 
    categoria = "SP", 
    pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport3.jpg", 
    sexo = "ELLA", 
    n_pics = 0,
)
a.save()

a = Item(
    nombre = "Producto 4", 
    precio = 350, 
    categoria = "SP", 
    pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport4.jpg", 
    sexo = "ELLA", 
    n_pics = 0,
)
a.save()

a = Item(
    nombre = "Producto 5", 
    precio = 350, 
    categoria = "SP", 
    pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport5.jpg", 
    sexo = "ELLA", 
    n_pics = 0,
)
a.save()

a = Item(
    nombre = "Producto 6", 
    precio = 350, 
    categoria = "SP", 
    pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport6.jpg", 
    sexo = "ELLA", 
    n_pics = 0,
)
a.save()

a = Item(
    nombre = "Producto 7", 
    precio = 350, 
    categoria = "SP", 
    pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport7.jpg", 
    sexo = "ELLA", 
    n_pics = 0,
    color_disp = "Rojo,Azul Cielo,Turqueza,Amarillo,Rosa mexicano"
)
a.save()

