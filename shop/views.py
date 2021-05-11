from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import datetime
from django.db import IntegrityError
from random import randint
from .models import User, Item, Carrito, Pedido

def index(request):
    #Inicializar variable 
    request.session["message"] = False
    #Render main page
    return render(request,"shop/home.html",{})

def sport(request): 
    #Inicializar variable 
    request.session["message"] = False
    if request.method == "GET": 
        #Query database for sport items
        sports = Item.objects.filter(categoria="SP")
        #Render sport page
        return render(request,"shop/sports.html", {
            "sports" : sports
        })    

    else:
        # User wants to see an item  
        item_id = request.POST["item_id"]
        # Save to session item_id and redirect to view page
        request.session['item_id'] = item_id
        return redirect('view')

def view(request): 

    if request.method == "GET": #Show item details
        # Query item
        item_id = request.session['item_id']
        aitem = Item.objects.get(id = item_id)
        # Image adress vector post procesing
        n_pics = aitem.n_pics
        pic_adress = []
        for i in range(0,n_pics):
            pic_name = "pic" + str(i + 1)
            pic_adress.append(getattr(aitem,pic_name))
        # Render view page
        return render(request, "shop/item.html", {
            "pic_adress" : pic_adress,
            "item" : aitem
        })

    else: # Añadir al carrito
    
        #Redirect to login if user is not logged in
        if request.user.id is None:
            request.session['fromitem'] = True
            return redirect('login')

        #Do add item ro carrito
        else:
            #Get information of item from form
            talla = request.POST["talla"]
            cantidad = request.POST["cantidad"]
            item_id = request.session['item_id'] #Lets be careful here...
            #Validar talla y cantidad
            if talla == "TALLA" or cantidad == "CANTIDAD":
                messages.warning(request, 'Selecciona talla y cantidad.')

                return redirect('view')

            else:
                #Agregar al carrito
                carro = Carrito(
                    item = Item.objects.get(id = item_id),
                    cantidad = cantidad,
                    talla = talla,
                    user = User.objects.get(id=request.user.id)
                    )
                carro.save()
                #Redireccionar al carrito
                return redirect('carrito')

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request,"Usuario o contraseña invalidos")
            return render(request, "shop/login.html")
    else:
        return render(request, "shop/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.warning(request, " Las contraseñas no coinciden ")
            return render(request, "shop/register.html", )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error(request,"Nombre de usuario no disponible")
            return render(request, "shop/register.html")

        login(request, user)
        #Para que se marque "Agrega tu información de usuario para poder comprar"
        request.session["message"] = True
        return HttpResponseRedirect(reverse('user'))
    else:
        return render(request, "shop/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))        

@login_required
def carrito(request):

    if request.method == "GET": # Mostrar carrito
        #Query items of cart for logged user
        user = User.objects.get(id=request.user.id)
        carrito = Carrito.objects.filter(user = request.user.id) #For some reason works well with user it, and wont accept a user object
        #Carrito vacío?
        empty = False
        if len(carrito) == 0:
            empty = True
        subtotal = 0
        #Calculando el subtotal
        for row in carrito:
            subtotal = subtotal + row.cantidad * row.item.precio  
        return render(request, "shop/cart.html", {
            "carrito" : carrito, 
            "subtotal" : subtotal, 
            "empty" : empty
        } )

    else:

        #Finalizar compra?
        fin = request.POST["fin"]

        if fin == "terminar":

            #If user has no adress, do not proceed
            user = User.objects.get(id = request.user.id)
            adress = user.direccion
            if not adress:
                messages.warning(request, "Por favor actualiza tu información de dirección y contacto para poder comprar")
                return redirect('user')

            #Pasar carrito de user a tabla de pedidos
            temp = Carrito.objects.filter(user = User.objects.get(id = request.user.id))
            identifier = randint(1111,9999)
            for entry in temp:
                pedido = Pedido(
                    item = entry.item,
                    cantidad = entry.cantidad, 
                    talla = entry.talla, 
                    color = entry.color,
                    user = entry.user, 
                    estatus = "Pedido", 
                    fecha = datetime.datetime.now(), 
                    folio = 0, 
                    identifier = identifier
                )
                pedido.save()
            #Limpiar carrito 
            temp.delete()

            #Pedir usuario que mande comprobante de compra a usuario?
            #Crear master account para ver pedidos e información de usuarios
            return redirect('pedidos')

        else:
            #Quitar del carrito elemento con id: cart_id
            cart_id = request.POST['cart_id']
            todrop = Carrito.objects.get(id = cart_id)
            todrop.delete()

            return redirect('carrito')

@login_required
def pedidos(request):

    if request.method == "GET":
        # MOSTRAR PEDIDOS ()
        #Check items on pedidos
        pedidos = Pedido.objects.filter(user = User.objects.get(id = request.user.id))
        #If no pedidos, say so
        empty = False
        if len(pedidos) == 0:
            empty = True
            return render(request, "shop/pedidos.html", {
                "empty":empty 
            } )
        # Ordenar pedidos por fecha y calcular monto
        ped_ord = [] #Fechas de conjuntos de pedidos ordenadas
        ped_sets = [] # Sets de pedidos ordenados por fecha tal como en ped_ord
        total = [] # Sets de precios totoales correspodientes a ped_sets
        subtotal = 0
        temp = [] #Temporary list to append set to ped_sets
        idenfifier = pedidos.first().identifier #Fecha del primer pedido  ########################### CHEACAR ESTE LOOP 
        for pedido in pedidos:
            if idenfifier == pedido.identifier:
                temp.append(pedido)
                subtotal = subtotal + pedido.cantidad * pedido.item.precio
            else:
                #Close last set of items with the same date:
                ped_ord.append(idenfifier)
                ped_sets.append(temp)
                total.append(subtotal)
                #Reiniciar vairables temporales
                temp = []
                subtotal = 0    
                #Start new list of items with the same date:
                temp.append(pedido)
                subtotal = subtotal + pedido.cantidad * pedido.item.precio
                #Update date
                idenfifier = pedido.identifier
        #Close final list:
        ped_ord.append(idenfifier)
        ped_sets.append(temp)
        total.append(subtotal)
    
        if request.session["message"]:
            messages.warning(request, "Folio actualizado correctamente. Nuestro staff revisara tu pago, y lo verificará a la brevedad")
            request.ssession["message"] = False
        return render(request, "shop/pedidos.html", {
            "ped_master" : zip(ped_ord,total,ped_sets), 
            "empty": empty
        } )


    else: #User va a subir el folio 

        date = request.POST["no_pedido"] #Corresponde a date
        folio = request.POST["Folio"]
        # Añadir folio a pedido correspondiente a la fecha date
        pedidos = Pedido.objects.filter(item = Item.objects.filter(fecha = date))
        for pedido in pedidos: 
            pedido.folio = folio
            pedido.estatus = "Pago en renvisión"
            pedido.save()
        #Flash message of pedido
        request.session["message"] = True
        return redirect("/pedidos")

@login_required
def user(request):

    if request.method == "GET":
        #Get user info
        info = User.objects.get(id=request.user.id)
        if request.session["message"]: 
            messages.info(request, "Añade tu información de dirección y contacto para poder comprar")
            request.session["message"] = False 
        return render(request,"shop/user.html", {
            "info": info
        })

    else:
        #User is trying to update information
        #Suppose information is correctly formated
        #Probably, sanitize inputs in the future

        #Update user information
        userinfo = User.objects.get(id = request.user.id)
        userinfo.nombre = request.POST["name"]
        userinfo.cpp = request.POST["cp"]
        userinfo.telefono = request.POST["phone"]
        userinfo.direccion = request.POST["adress"]
        userinfo.save()

        #Info Updated
        messages.success(request, "Información de usuario actualizada correctamente")

        #Get info
        return redirect('user')

            # return render(request, "shop/apology.html", {
            # "mesage" :
            #  })

@staff_member_required
def master(request):
    if request.method == "GET" :
        #Mostrar pedidos master
        #Check items on pedidos
        pedidos = Pedido.objects.all()
        #If no pedidos, say so
        empty = False
        if len(pedidos) == 0:
            empty = True
            return render(request, "shop/master.html", {
                "empty":empty 
            } )
        # Ordenar pedidos por fecha y calcular monto
        ped_ord = [] #Fechas de conjuntos de pedidos ordenadas
        ped_sets = [] # Sets de pedidos ordenados por fecha tal como en ped_ord
        total = [] # Sets de precios totoales correspodientes a ped_sets
        subtotal = 0
        temp = [] #Temporary list to append set to ped_sets
        hack = [] #Primer pedido de cada usuario
        idenfifier = pedidos.first().identifier #Fecha del primer pedido  ########################### CHEACAR ESTE LOOP 
        hack.append(pedidos.first())
        for pedido in pedidos:
            if idenfifier == pedido.identifier:
                temp.append(pedido)
                subtotal = subtotal + pedido.cantidad * pedido.item.precio
            else:
                #Close last set of items with the same identifier
                hack.append(pedido)
                ped_ord.append(idenfifier)
                ped_sets.append(temp)
                total.append(subtotal)
                #Reiniciar vairables temporales
                temp = []
                subtotal = 0    
                #Start new list of items with the same date:
                temp.append(pedido)
                subtotal = subtotal + pedido.cantidad * pedido.item.precio
                #Update date
                idenfifier = pedido.identifier
        #Close final list:
        ped_ord.append(idenfifier)
        ped_sets.append(temp)
        total.append(subtotal)

        # return render(request, "shop/apology.html", {
        # "ped_master" : zip(ped_ord,total,ped_sets), 
        # "ped_ord" : ped_ord, 
        # "total" : total,
        # "ped_sets" : ped_sets, 
        # "hack": hack
        #  })

        return render(request, "shop/master.html", {
            "ped_master" : zip(hack,ped_ord,total,ped_sets), 
            "empty": empty
        } )

    else:
        estatus = request.POST["estatus"]
        identifier = request.POST["identifier"]
        user_id = request.POST["user"]
        #Actualizar estatus en base de datos
        pedidos = Pedidos.objects.filter(idenfifier = identifier, user = User.objects.get(id = user_id))
        for pedido in pedidos: 
            pedido.estatus = estatus
            pedido.save()
        return redirect('master')



            # return render(request, "shop/apology.html", {
    #     "ped_master" : zip(ped_ord,total,ped_sets), 
    #     "ped_ord" : ped_ord, 
    #     "total" : total,
    #     "ped_sets" : ped_sets
    #      })