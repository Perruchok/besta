# This piece of code Populates the existing database
# I do this so I dont have to do it manually at admin site.

from shop.models import Item

def main():

    # ------------------------------   SPORT ITEMS -----------------------------------
    # a = Item(
    #     nombre = "Blusa sport", 
    #     precio = 350, 
    #     categoria = "SP", 
    #     pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport1.jpg", 
    #     sexo = "ELLA", 
    #     n_pics = 3,
    #     pic1 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport1_1.jpg",
    #     pic2 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport1_2.jpg", 
    #     pic3 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport1_3.jpg", 
    #     color_disp = "Azul,Caquis,Rosa",
    #     descripcion = "Buena para hacer ejercicio   "
    # )
    # a.save()

    # a = Item(
    #     nombre = "Producto 2", 
    #     precio = 350, 
    #     categoria = "SP", 
    #     pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport2.jpg", 
    #     sexo = "ELLA", 
    #     n_pics = 2,
    #     pic1 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport2_1.jpg",
    #     pic2 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport2_2.jpg", 
    #     color_disp = "Blanco Liso, Rojo pasion"
    # )
    # a.save()

    # a = Item(
    #     nombre = "Producto 3", 
    #     precio = 350, 
    #     categoria = "SP", 
    #     pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport3.jpg", 
    #     sexo = "ELLA", 
    #     n_pics = 0
    # )
    # a.save()

    # a = Item(
    #     nombre = "Producto 4", 
    #     precio = 350, 
    #     categoria = "SP", 
    #     pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport4.jpg", 
    #     sexo = "ELLA", 
    #     n_pics = 0
    # )
    # a.save()

    # a = Item(
    #     nombre = "Producto 5", 
    #     precio = 350, 
    #     categoria = "SP", 
    #     pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport5.jpg", 
    #     sexo = "ELLA", 
    #     n_pics = 0
    # )
    # a.save()

    # a = Item(
    #     nombre = "Producto 6", 
    #     precio = 350, 
    #     categoria = "SP", 
    #     pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport6.jpg", 
    #     sexo = "ELLA", 
    #     n_pics = 0
    # )
    # a.save()

    # a = Item(
    #     nombre = "Producto 7", 
    #     precio = 350, 
    #     categoria = "SP", 
    #     pic0 = "https://raw.githubusercontent.com/Perruchok/besta_pictures/main/sport/sport7.jpg", 
    #     sexo = "ELLA", 
    #     n_pics = 0,
    #     color_disp = "Rojo,Azul Cielo,Turqueza,Amarillo,Rosa mexicano", 
    # )
    # a.save()

    a = Item(
    nombre = "Short ajustable", 
    precio = 300, 
    categoria = "SP", 
    pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva1.JPG", 
    sexo = "", 
    n_pics = 3,
    pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva1_1.JPG",
    pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva1_2.JPG", 
    pic3 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva1_3.JPG", 
    color_disp = "negro, amarillo, rojo, rosa mexicano, azul rey, verde menta",
    descripcion = "Short deportivo que llega hasta media pierna, Contiene tiras a los costados que ajustan la altura del short haciéndolo más corto."
    )
    a.save()

    a = Item(
        nombre = "Top básico",
        precio = 200,
        categoria = "SP",
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva2.PNG", 
        sexo = "", 
        n_pics = 1,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva2_1.PNG",
        color_disp = "negro, amarillo, rojo, rosa mexicano, azul rey, verde menta",
        descripcion = "Top de licra de colores brillantes, ideal para hacer ejercicio o para un look más formal.",
    )
    a.save()

    a = Item(
        nombre = "Top deportivo", 
        precio = 200, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva3.JPG", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva3_1.JPG",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva3_2.JPG",
        color_disp = "negro, amarillo, rojo, rosa mexicano, azul rey, verde menta",
        descripcion = "Top deportivo que llega a la cintura. Cómodo para entrenar y para vestir casual."
    )
    a.save()

    a = Item(
        nombre = "Top de lado", 
        precio = 300, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva4.PNG", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva4_1.PNG",
        color_disp = "negro, amarillo, rojo, rosa mexicano, azul rey, verde menta",
        descripcion = "Top con ambos tirantes del lado derecho. Úsalo para salir o para ejercitarte."
    )
    a.save()

    a = Item(
        nombre = "Short biker", 
        precio = 350, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva5.PNG", 
        sexo = "él, ella", 
        n_pics = 3,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva5_1.PNG",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva5_2.PNG",
        pic3 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva5_3.PNG",
        color_disp = "negro, amarillo, rojo, rosa mexicano, azul rey, verde menta",
        descripcion = "Short que llega arriba de la rodilla. Ideal para rodar y lucir cool. Puedes pedir el modelo 'él' para mayor espacio en la entrepierna."
    )
    a.save()

    a = Item(
        nombre = "Top resorte", 
        precio = 200, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva6.PNG", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva6_1.PNG",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva6_2.PNG",
        color_disp = "negro, amarillo, rojo, rosa mexicano, azul rey, verde menta",
        descripcion = "Top con tirantes coquetos. Te hará lucir lindx en cualquier ocasión."
    )
    a.save()

    a = Item(
        nombre = "Blusa mesh", 
        precio = 250, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva7.JPG", 
        sexo = "manga corta, manga larga", 
        n_pics = 6,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva7_1.JPG",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva7_2.JPG", 
        pic3 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva7_3.JPG", 
        pic4 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva7_4.JPG",
        pic5 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva7_5.JPG", 
        pic6 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva7_6.JPG",
        color_disp = "negro, blanco, arena",
        descripcion = "Blusa de elástica de mesh. Úsala encima de alguna prenda o sola. Puedes elegir manga corta o manga larga."
    )
    a.save()

    a = Item(
        nombre = "Rompevientos", 
        precio = 400, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva8.JPG", 
        sexo = "", 
        n_pics = 5,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva8_1.JPG",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva8_2.JPG", 
        pic3 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva8_3.JPG", 
        pic4 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva8_4.JPG", 
        pic5 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva8_5.JPG", 
        color_disp = "negro, azul cielo, morado, amarillo neón. naranja neón",
        descripcion = "Chamarra rompevientos y repelente al agua. Es muy ligera y ocupa poco espacio. Llévala cuando salgas a correr y quieras lucir bien."
    )
    a.save()

    a = Item(
        nombre = "Leotardo", 
        precio = 200, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva9.JPG", 
        sexo = "", 
        n_pics = 2,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva9_1.JPG",
        pic2 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva9_2.JPG", 
        color_disp = "negro, azul marino, azul pastel, rojo, rosa pastel, rosa mexicano, guinda",
        descripcion = "Leotardo básico de tirantes y escote a la espalda baja. Fábricado con tela muy cómoda para bailar."
    )
    a.save()

    a = Item(
        nombre = "Playera algodón", 
        precio = 250, 
        categoria = "SP", 
        pic0 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva10.PNG", 
        sexo = "", 
        n_pics = 1,
        pic1 = "https://raw.githubusercontent.com/YURIHW/besta_pictures/main/Dep/Deportiva1_1.JPG",
        color_disp = "negro, gris, azul, morado, verde, amarillo, rojo, rosa mexicano, beige, blanco",
        descripcion = "Playera manga corta con corte especial en la bastilla. El básico que le hacía falta a tu closet. Sus fibras de algodón ofrecen una textura suave al tacto."
    )
    a.save()

    # ------------------------------   TWERK ITEMS -----------------------------------

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

