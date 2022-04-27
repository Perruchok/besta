# This piece of code Populates the existing database
# I do this so I dont have to do it manually at admin site.

from shop.models import Item

def main():
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
        n_pics = 0
    )
    a.save()

    a = Item(
        nombre = "Producto 4", 
        precio = 350, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport4.jpg", 
        sexo = "ELLA", 
        n_pics = 0
    )
    a.save()

    a = Item(
        nombre = "Producto 5", 
        precio = 350, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport5.jpg", 
        sexo = "ELLA", 
        n_pics = 0
    )
    a.save()

    a = Item(
        nombre = "Producto 6", 
        precio = 350, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport6.jpg", 
        sexo = "ELLA", 
        n_pics = 0
    )
    a.save()

    a = Item(
        nombre = "Producto 7", 
        precio = 350, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport7.jpg", 
        sexo = "ELLA", 
        n_pics = 0,
        color_disp = "Rojo,Azul Cielo,Turqueza,Amarillo,Rosa mexicano", 
    )
    a.save()

    a = Item(
        nombre = "Short flojo", 
        precio = 400, 
        categoria = "TW", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk1.jpg", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk1_1.jpg",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk1_2.jpg", 
        color_disp = "Naranja neón",
        descripcion = "Fabricado con tela de algodón. Su diseño cruzado favorece el movimiento.",
    )
    a.save()

    a = Item(
        nombre = "Short cachetero", 
        precio = 400, 
        categoria = "TW", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk2.jpg", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk2_1.jpg",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk2_2.jpg", 
        color_disp = "Animal print, arcoíris, vaquita, fuego",
        descripcion = "Short de licra que llega hasta la mitad del glúteo, cuenta con resorte en la parte de atrás para aumentar el volumen. Fabricado con tela que permite un buen rango de movimiento a la hora de twerkear.",
    )
    a.save()

    a = Item(
        nombre = "Short biker", 
        precio = 600, 
        categoria = "TW", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk3.jpg", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk3_1.jpg",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk3_2.jpg", 
        color_disp = "Animal print, arcoíris, vaquita, fuego",
        descripcion = "Short de licra que llega unos centímetros arriba de la rodilla. Prenda básica del outfit. Cómodo para bailar o realizar cualquier deporte.",
    )
    a.save()

    a = Item(
        nombre = "Short ajustable", 
        precio = 500, 
        categoria = "TW", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk4.jpg", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk4_1.jpg",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk4_2.jpg", 
        color_disp = "Azul, rosa neón, amarillo neón",
        descripcion = "Short de licra anticloro con cintas ajustables a los costados que permiten modificar lo largo del short. Cuenta con resorte en medio de los glúteos para aumentar el volumen.",
    )
    a.save()

    a = Item(
        nombre = "Top doble vista", 
        precio = 400, 
        categoria = "TW", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk5.jpg", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk5_1.jpg",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk5_2.jpg", 
        color_disp = "Rosa neón y amarillo neón, rosa neón y azul, amarillo neón y azul",
        descripcion = "Top fabricado con tela anticloro, y lo mejor ¡lo puedes usar por ambos lados!",
    )
    a.save()

    a = Item(
        nombre = "Top estampado", 
        precio = 400, 
        categoria = "TW", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk6.jpg", 
        sexo = "", 
        n_pics = 3,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk6_1.jpg",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk6_2.jpg", 
        pic3 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk6_3.jpg", 
        color_disp = "Animal print, arcoíris, vaquita, fuego",
        descripcion = "Top deportivo hasta la cintura. Fabricado con tela estampada.",
    )
    a.save()

    a = Item(
        nombre = "Torera", 
        precio = 450, 
        categoria = "TW", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk7.jpg", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk7_1.jpg",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk7_2.jpg", 
        color_disp = "Amarillo neón, negro, blanco",
        descripcion = "Torera de manga larga con escote al frente. Fabricada con tela de algodón.",
    )
    a.save()

    a = Item(
        nombre = "Rodilleras", 
        precio = 300, 
        categoria = "TW", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk8.jpg", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk8_1.jpg",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Twerk/twerk8_2.jpg", 
        color_disp = "Amarillo neón, negro, gris",
        descripcion = "Protectores de rodilla, ideales para trapear el inframundo con los glúteos sin lastimarte.",
    )
    a.save()

if __name__ == "__main__":
    main()

