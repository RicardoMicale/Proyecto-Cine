#Codigo principal donde se exportan las clases y se hacen las funciones
from Pelicula import Pelicula 
from Cliente import Cliente
from Producto import Producto
from Combo import Combo
#3 clases importadas
#Primera funcion: crear cada pelicula
peliculas = [] #Lista general de todas las peliculas
clientes = [] #Lista general de clientes
productos = [] #Lista general de lo que se vende en la caramelería 
combos = [] #Lista general de combos
costos = [] #Lista de gastos de cada cliente
costos_carameleria = [] #Lista de los gastos en caramelería
chucherias_compradas = [] #Lista de las chucherias que se compran
u, v, w, x, y, z = (0, 1, 2, 3, 4, 5) #Tupla de indices para devolver el asiento si el cliente no procede con su compra
salas = ["2D","3D","4DX","VIP"]
sala1 = [
    ["1A","2A","3A","4A","5A"],
    ["1B","2B","3B","4B","5B"],
    ["1C","2C","3C","4C","5C"],
    ["1D","2D","3D","4D","5D"],
    ["1E","2E","3E","4E","5E"]] #Lista para el mapa de la sala 1
sala2 = [
    ["1A","2A","3A","4A","5A","6A"],
    ["1B","2B","3B","4B","5B","6B"],
    ["1C","2C","3C","4C","5C","6C"],
    ["1D","2D","3D","4D","5D","6D"],
    ["1E","2E","3E","4E","5E","6E"],
    ["1F","2F","3F","4F","5F","6F"]] #Lista para el mapa de la sala 2
sala3 = [
    ["1A","2A","3A","4A"],
    ["1B","2B","3B","4B"],
    ["1C","2C","3C","4C"],
    ["1D","2D","3D","4D"]] #Lista para el mapa de la sala 3
sala4 = [
    ["1A","2A","3A"],
    ["1B","2B","3B"],
    ["1C","2C","3C"]] #Lista para el mapa de la sala 4

#MODULO DE PELÍCULAS
def crear_pelicula():
    """
    Esta función crea cada pelicula y la define como objeto
    """
    t = True
    while t:    
        titulo = input("Título de la pelicula: ").title()
        if len(peliculas) > 0:
            for pelicula in peliculas:
                if titulo == pelicula.titulo:
                    print("Pelicula ya agregada a la cartelera")
                    t = True
                else:
                    t = False
        elif titulo == "" or titulo == " ":
            print("El nombre de la pelicula no es válido")
        elif len(peliculas) == 0:
            break
    director = input("Quien es el director de la pelicula: ").title()
    while True:
        clasificacion = input("Indique la clasificación de la película (A, B, C o D): ").upper()
        if clasificacion == "A" or clasificacion == "B" or clasificacion == "C" or clasificacion == "D": #Verifica que la clasificacion sea válida
            break
        else:
            print("Clasificacion no válida.")
    while True:
        imdb = input("Indique el puntaje de la película según IMDB (1 al 10 y separado por puntos): ")
        if imdb.replace(".","",1).isdigit(): #Verifica que el puntaje sean numeros 
            imdb = float(imdb) # convierte en float para que el siguiente if se pueda comprobar
            if imdb > 0.0 and imdb <= 10.0: #Verifica que esten entre el minimo y el maximo establecido
                break
            else:
                print("El número que ingresó es menor que 1 o mayor que 10. Por favor ingrese otro.")
        else:
            print("Puntaje no válido. El puntaje debe estar entre 1 y 10 y separado por puntos")
    reparto = []
    while True:
        x = input("Cantidad de actores con un papel principal: ")
        if x.isdecimal():
            while True:
                actor = input("Cual o cuales son los actores principales: ").title()
                reparto.append(actor)
                if len(reparto) == int(x):
                    break
            break
        else:
            print("La cantidad de actores debe ser un número entero")
    genero = input("Genero de la película: ").title()
    print("Salas disponibles: ")
    for i in salas:
        print(i) #Muestra las salas que hay
    i = 0
    sala = input("En que sala se puede ver la película: ").upper() #Uso del metodo upper para que al momento de chequear la lista, las letras coincidan
    while i < len(salas):
        if sala == salas[i]:
            salas.pop(i) #Si la sala que se selecciona esta disponible se quita de la lista
            break
        elif sala not in salas:
            print("Ingrese una sala existente") #Validacion de las salas existentes, si es diferente de las salas en la lista
            sala = input("En que sala se puede ver la película: ").upper() #Se vuelve a pedir el input para redefinirla
        else:
            i += 1
    pelicula = Pelicula(titulo,director,clasificacion,imdb,reparto,genero,sala)
    return pelicula

def mapa_1(sala1):
    """
    Función para mostrar el mapa de la sala 1
    """
    print("Sala 2D, asientos disponibles:")
    print("        [PANTALLA]       ")
    i = 0
    while i < len(sala1):
        hileras = sala1[i]
        print("({}) ({}) ({}) ({}) ({})".format(hileras[0],hileras[1],hileras[2],hileras[3],hileras[4]))
        i += 1

def mapa_2(sala2):
    """
    Función para mostrar el mapa de la sala 2
    """
    print("Sala 3D, asientos disponibles:")
    print("        [PANTALLA]       ")
    i = 0
    while i < len(sala2):
        hileras = sala2[i]
        print("({}) ({}) ({}) ({}) ({}) ({})".format(hileras[0],hileras[1],hileras[2],hileras[3],hileras[4],hileras[5]))
        i += 1

def mapa_3(sala3):
    """
    Función para mostrar el mapa de la sala 3
    """
    print("Sala 4DX, asientos disponibles:")
    print("     [PANTALLA]  ")
    i = 0
    while i < len(sala3):
        hileras = sala3[i]
        print("({}) ({}) ({}) ({})".format(hileras[0],hileras[1],hileras[2],hileras[3]))
        i += 1  

def mapa_4(sala4):
    """
    Función para mostrar el mapa de la sala 4
    """
    print("Sala VIP, asientos disponibles:")
    print("  [PANTALLA]  ")
    i = 0
    while i < len(sala4):
        hileras = sala4[i]
        print("({}) ({}) ({})".format(hileras[0],hileras[1],hileras[2]))
        i += 1

def filtro_pelicula():
    """
    Función para filtrar la busqueda de peliculas
    """
    while True: #While loop para verificar los filtros e imprimir las peliculas segun el filtro que se ponga
        print("-"*60)
        filtro = input(
            "Desea aplicar alguno de los siguientes filtros para la busqueda de peliculas? Indicar (Género, Rating, Actor o Director): "
        ).lower()
        print("-"*60)
        if filtro == "genero" or filtro == "género":
            filtro_g = input("Indique el género de películas: ").title()
            for pelicula in peliculas:
                if pelicula.genero == filtro_g: #Revisa el genero en cada pelicula y la compara con el que se pidio
                    print("-"*60)
                    pelicula.descripcion_pelicula() #Solo muestra las que coincidan
                    print("-"*60)
        elif filtro == "rating":
            filtro_r = float(input("Indique el rating minimo: "))
            for pelicula in peliculas: 
                if pelicula.imdb >= filtro_r: #Revisa el rating de cada película y verifica que sea mayor que el que se especifica
                    print("-"*60)
                    pelicula.descripcion_pelicula() #Solo muestra las que coincidan
                    print("-"*60)
        elif filtro == "actor":
            filtro_a = input("Indique el actor que quiere buscar: ").title()
            for pelicula in peliculas:
                for actor in pelicula.reparto:
                    if actor == filtro_a: #Revisa el reparto y lo compara con el actor, dentro de la lista del reparto, que se busca
                        print("-"*60)
                        pelicula.descripcion_pelicula() #Solo muestra las que coincidan
                        print("-"*60)
        elif filtro == "director": 
            filtro_d = input("Indique el director que quiere buscar: ").title()
            for pelicula in peliculas: 
                if pelicula.director == filtro_d: #Revisa el director y lo compara con el que se busca
                    print("-"*60)
                    pelicula.descripcion_pelicula() #Solo muestra las que coincidan
                    print("-"*60)
        elif filtro == "no" or filtro == "n":
            for pelicula in peliculas: #Muestra todas las peliculas en cartelera
                print("-"*60)
                pelicula.descripcion_pelicula()
                print("-"*60)
        else:
            print("Seleccione un filtro válido o indique que no")
        otro = input("Desea aplicar un filtro diferente? (Si o No) ").lower() 
        #Si no se busca otro filtro se pasa directo a la compra del ticket, sino se devuelve al menu de filtros
        if otro == "n" or otro == "no":
            break

#MODULO DE CARAMELERÍA
def crear_producto():
    """
    Funcion para crear los productos de la caramelería
    Los define como objetos
    """
    nombre = input("Nombre del producto: ").title()
    while True:
        tipo = input("Indique el tipo de producto (Comida o bebida): ").title()
        if tipo == "Comida": #Dependiendo del tipo de producto se pide una caracteristica diferente
            caracteristica = input("Es una comidad de preparacion o de empaque: ").title()
            break
        elif tipo == "Bebida":
            caracteristica = input("Indique el tamaño de la bebida (pequeño, mediano, grande): ").title()
            break
        else:
            print("Selecione un tipo de alimento válido")
    while True:    
        precio = input("Indique el precio del producto (En Bs y si es decimal, separado por puntos): ")
        if precio.replace(".","",1).isdigit():
            precio = float(precio)
            if precio <= 0.0:
                print("El precio debe ser mayor a 0. Ingrese un precio válido")
            else:
                break
        else:
            print("El precio debe ser un número, si es decimal separado por puntos. Ingrese un precio válido")
    producto = Producto(nombre,tipo,caracteristica,precio)
    return producto

def crear_combo():
    """
    Crear cada combo y definirlos como objetos
    """
    nombre_combo = input("Indique el nombre del combo: ").title()
    productos = [] 
    while True:
        z = input("Ingrese la cantidad de productos que hay en el combo (mínimo 2): ")
        if z.isdecimal():
            z = int(z)
            if z > 1:
                while True:
                    producto = input("Indique los productos que se venden en el combo: ").title()
                    productos.append(producto)
                    if z == len(productos):
                        break
                break
            elif z == 1 or z == 0:
                print("Ingresó un número de productos menor a 2. Ingrese otro número")
        else:
            print("Cantidad no válida. Ingrese un número como cantidad")
    while True:    
        monto = input("Indique el precio del combo (En Bs y si es decimal, separado por puntos): ")
        if monto.replace(".","",1).isdigit():
            monto = float(monto)
            if monto <= 0.0:
                print("El precio debe ser mayor a 0. Ingrese un precio válido")
            else:
                break
        else:
            print("El precio debe ser un número, si es decimal separado por puntos. Ingrese un precio válido")
    combo = Combo(nombre_combo,productos,monto)
    return combo

def filtro_producto():
    """
    Función para filtrar la búsqueda de productos
    """
    while True:
        filtro_prod = input(
            "Desea aplicar alguno de los siguientes filtros para la busqueda de productos o no? (Nombre, rango de precio) "
        ).lower()
        if len(productos) > 0:
            if filtro_prod == "nombre":
                filtro_n = input("Ingrese el nombre del producto que quiere buscar: ").title()
                for producto in productos:
                    print("aqui")
                    if filtro_n == producto.nombre: #Verifica que el nombre que se ingresó sea igual al del producto
                        print("-"*60)
                        producto.descrip_producto()
                        print("-"*60)
            elif filtro_prod == "rango de precios" or filtro_prod == "rango":
                while True:    
                    filtro_rgo = input("Ingrese el precio mas bajo del rango que quiere buscar: ")
                    filtro_rgo2 = input("Ingrese el precio mas alto del rango que quiere buscar: ")
                    if (filtro_rgo.replace(".","",1).isdigit() and filtro_rgo2.replace(".","",1).isdigit()) or (filtro_rgo.isdecimal() and filtro_rgo2.isdecimal()): #Verifica que las cantidades sean números
                        filtro_rgo = float(filtro_rgo) #Si ambos son números se convierten en float
                        filtro_rgo2 = float(filtro_rgo2)
                        break
                    else:
                        print("Uno o ninguno de los precios no es válido. El precio debe ser un número, si es decimal debe estar separado por puntos")
                for producto in productos:
                    if producto.precio > filtro_rgo and producto.precio < filtro_rgo2: #Verifica que los precios esten en el rango
                        print("-"*60)
                        producto.descrip_producto()
                        print("-"*60)
            elif filtro_prod == "n" or filtro_prod == "no": #Si no se pone un filtro se muestran todos
                for producto in productos:
                    print("-"*60)
                    producto.descrip_producto()
                    print("-"*60)
            else:
                print("Ingrese un filtro válido")
            otro_filtro = input("Desea buscar con otro filtro? (Si o No) ")
            if otro_filtro == "n" or otro_filtro == "no":
                break
        else:
            print("Lo sentimos, en este momento no hay productos a la venta")

def filtro_combo():
    """
    Funcion para filtrar los combos
    """
    while True:
        filtro_com = input(
            "Desea aplicar alguno de los siguientes filtros para la busqueda de combos o no? (Nombre, rango de precio) "
        ).lower()
        if len(combos) > 0:
            if filtro_com == "nombre":
                filtro_n = input("Ingrese el nombre del combo que quiere buscar: ").title()
                for combo in combos:
                    if combo.nombre_combo == filtro_n:
                        print("-"*60)
                        combo.descrip_combo()
                        print("-"*60)
            elif filtro_com == "rango de precios":
                while True:    
                    filtro_rgo = input("Ingrese el precio mas bajo del rango que quiere buscar: ")
                    filtro_rgo2 = input("Ingrese el precio mas alto del rango que quiere buscar: ")
                    if filtro_rgo.replace(".","",1).isdigit() and filtro_rgo2.replace(".","",1):
                        filtro_rgo = float(filtro_rgo)
                        filtro_rgo2 = float(filtro_rgo2)
                        break
                    else:
                        print("Uno o ninguno de los precios no es válido. El precio debe ser un número, si es decimal debe estar separado por puntos")
                for combo in combos:
                    if combo.monto > filtro_rgo and combo.monto < filtro_rgo2:
                        print("-"*60)
                        combo.descrip_combo()
                        print("-"*60)
            elif filtro_com == "n" or filtro_com == "no":
                for combo in combos:
                    print("-"*60)
                    combo.descrip_combo()
                    print("-"*60)
            else:
                print("Ingrese un filtro válido")
            otro_filtro = input("Desea buscar con otro filtro? (Si o No) ")
            if otro_filtro == "n" or otro_filtro == "no":
                break
        else:
            print("Lo sentimos, en este momento no hay combos disponibles")

#MODULO DE VENTA DE TICKETS
def asiento1(sala1):
    """
    Funcion para elegir asientos en la sala 1 (2D)
    """
    num_asiento = ["1","2","3","4","5"]
    letra_asiento = ["A","B","C","D","E"]
    mapa_1(sala1)
    t = True
    while t:
        i = 0
        asiento = input("Seleccione el asiento que quiere comprar: ").upper()
        while i < len(sala1):
            hileras = sala1[i]
            if asiento in hileras:
                if asiento == "XX":
                    print("Asiento ocupado. Seleccione otro")
                    i += 1
                else:
                    compra_asiento = input("Seguro que quiere comprar ese asiento? (Si o No) ").lower()
                    if compra_asiento == "si" or compra_asiento == "s":
                        hileras[hileras.index(asiento)] = "XX"
                        t = False
                        break
                    else:
                        break
            elif asiento[0] not in num_asiento or asiento[1] not in letra_asiento:
                print("El asiento que usted seleccionó no existe o está ocupado y marcado con una 'XX'. Seleccione uno que esté disponible")
                break
            else:
                i += 1
    return asiento

def asiento2(sala2):
    """
    Funcion para elegir asientos en la sala 2 (3D)
    """
    num_asiento = ["1","2","3","4","5","6"]
    letra_asiento = ["A","B","C","D","E","F"]
    mapa_2(sala2)
    t = True
    while t:
        i = 0
        asiento = input("Seleccione el asiento que quiere comprar: ").upper()
        while i < len(sala2):
            hileras = sala2[i]
            if asiento in hileras:
                if asiento == "XX":
                    print("Asiento ocupado. Seleccione otro")
                    i += 1
                else:
                    compra_asiento = input("Seguro que quiere comprar ese asiento? (Si o No) ").lower()
                    if compra_asiento == "si" or compra_asiento == "s":
                        hileras[hileras.index(asiento)] = "XX"
                        t = False
                        break
                    else:
                        break
            elif asiento[0] not in num_asiento or asiento[1] not in letra_asiento:
                print("El asiento que usted seleccionó no existe o está ocupado y marcado con una 'XX'. Seleccione uno que esté disponible")
                break
            else:
                i += 1
    return asiento

def asiento3(sala3):
    """
    Funcion para elegir asientos en la sala 3 (4DX)
    """
    num_asiento = ["1","2","3","4"]
    letra_asiento = ["A","B","C","D"]
    mapa_3(sala3)
    t = True
    while t:
        i = 0
        asiento = input("Seleccione el asiento que quiere comprar: ").upper()
        while i < len(sala3):
            hileras = sala3[i]
            if asiento in hileras:
                if asiento == "XX":
                    print("Asiento ocupado. Seleccione otro")
                    i += 1
                else:
                    compra_asiento = input("Seguro que quiere comprar ese asiento? (Si o No) ").lower()
                    if compra_asiento == "si" or compra_asiento == "s":
                        hileras[hileras.index(asiento)] = "XX"
                        t = False
                        break
                    else:
                        break
            elif asiento[0] not in num_asiento or asiento[1] not in letra_asiento:
                print("El asiento que usted seleccionó no existe o está ocupado y marcado con una 'XX'. Seleccione uno que esté disponible")
                break
            else:
                i += 1
    return asiento

def asiento4(sala4):
    """
    Funcion para elegir asientos en la sala 4 (VIP)
    """
    num_asiento = ["1","2","3"]
    letra_asiento = ["A","B","C"]
    mapa_4(sala4)
    t = True
    while t:
        i = 0
        asiento = input("Seleccione el asiento que quiere comprar: ").upper()
        while i < len(sala4):
            hileras = sala4[i]
            if asiento in hileras:
                if asiento == "XX":
                    print("Asiento ocupado. Seleccione otro")
                    i += 1
                else:
                    compra_asiento = input("Seguro que quiere comprar ese asiento? (Si o No) ").lower()
                    if compra_asiento == "si" or compra_asiento == "s":
                        hileras[hileras.index(asiento)] = "XX"
                        t = False
                        break
                    else:
                        break
            elif asiento[0] not in num_asiento or asiento[1] not in letra_asiento:
                print("El asiento que usted seleccionó no existe o está ocupado y marcado con una 'XX'. Seleccione uno que esté disponible")
                break
            else:
                i += 1
    return asiento

def crear_cliente():
    """
    Funcion para crear los clientes y definirlos como objetos
    """
    nombre = input("Nombre del cliente: ").title()
    while True:   
        cedula = input("Cédula del cliente: ")
        if cedula.isdecimal():
            cedula = int(cedula)
            if cedula > 1:
                cedula = str(cedula)
                break
            else:
                print("Ingrese una cédula válida. Solo pueden ser números mayores a 0 y sin decimales.")
        else:
            print("Ingrese una cédula válida. Solo pueden ser números mayores a 0 y sin decimales.")
    while True:    
        edad = input("Edad del cliente: ")
        if edad.isdecimal():
            edad = int(edad)
            break
        else:
            print("Ingrese una edad válida. Escriba su edad en años y sin decimales")
    p = True
    while p:
        i = 0
        peli = input("Indique el nombre de la pelicula que desea ver: ").title() #Pide la pelicula
        while True:
            if i > len(peliculas) - 1: #Si revisa todas los objetos de la lista se rompe el loop secundario y pregunta de nuevo hasta que entre una pelicula válida
                print("Pelicula no encontrada en cartelera. Seleccione otra")
                break
            pelicula = peliculas[i] #Define pelicula como uno de los objetos en la lista
            if peli == pelicula.titulo:
                seleccionar_peli = input("Seguro que quire esa película? (Si o No) ").lower()
                if seleccionar_peli == "s" or seleccionar_peli == "si":
                    p = False #Si estas seguro que quieres esa pelicula se define p (Condicion del primer loop) como falso  para que al romper el while secundario se deje de cumplir la condicion inicial
                    break #Rompe el while secundario 
                else:
                    break #Si no estas seguro de esa pelicula se rompe el while secundario sin romper el principal, haciendo que elijas otra pelicula
            else:
                i += 1
    while True:
        for pelicula in peliculas:
            if peli == pelicula.titulo: #Revisa cual es el titulo de la pelicula ingresada y busca su sala para dar la opcion de elegir asiento
                if pelicula.sala == "2D":
                    asiento = asiento1(sala1)
                elif pelicula.sala == "3D":
                    asiento = asiento2(sala2)
                elif pelicula.sala == "4DX":
                    asiento = asiento3(sala3)
                elif pelicula.sala == "VIP":
                    asiento = asiento4(sala4)
        break
    cliente = Cliente(nombre,cedula,edad,peli,asiento)
    return cliente

def abundante(precio_total):
    """
    Funcion para comprobar si el precio es un numero abundante
    """
    n = 1
    suma = 0
    while n < precio_total:
        if precio_total % n == 0:
            suma += n
        n += 1
    return suma

def capicua(cedula):
    """
    Funcion para verificar que la cedula es capicua
    """
    c = -1 
    igual = 0
    for x in range(0,len(cedula)//2):
        if cedula[x] == cedula[c]: #Usa el string de cedula para comprobar que los el numero sea capicula
            igual += 1 #Variable igual se suma solo si los numeros en posiciones opuestas son iguales
        c -= 1
    if igual >= len(cedula)/2: #Si la variable iguales es igual a la mitad del string de cédula, entonces es capicua
        return True
    else:
        return False

def num_primo(edad):
    """
    Funcion para saber si la edad es un número primo
    """
    divisores_primos = [] #Lista de divisores para verificar descuento
    d = 1
    while d < edad:
        if edad % d == 0: #Verifica que el numero que tiene "d" sea un divisor de la edad 
            d += 1
            divisores_primos.append(d) #Se agregan los divisores primos a una lista
        elif len(divisores_primos) > 2: #Cuando la,lista tenga 3 valores o mas, ya el numero no es primo y no aplica el descuento
            return False
        elif d >= edad/2 and len(divisores_primos) == 1: #cuando la variable "d" llega a la mitad de la edad se termina el loop ya que no van a haber mas divisores
            return True
        else:
            d += 1

def iva(precio):
    """
    Funcion para calcula el iva del precio de los productos
    """
    iva = precio * 0.16
    return precio + iva

#MODULO DE ESTADISTICAS 
def prom_gasto():
    """
    Funcion para calcular el promedio de gastos de los clientes
    """
    promedio = (sum(costos) + sum(costos_carameleria))/len(clientes)
    return promedio

def no_carameleria():
    """
    Funcion para calcular el porcentaje de gente que no compra chucherias
    """
    a = len(clientes) - len(costos_carameleria)
    no_chucherias = (a/len(clientes)) * 100
    return no_chucherias

def contador_peliculas():
    """
    Cuenta la cantidad de clientes por pelicula
    Retorna las 3 películas más taquilleras
    """
    contadores = {} #Diccionario vacío
    pelicula_1 = peliculas[0] #Se define pelicula 1 como la primera de la lista
    pelicula_2 = peliculas[1]
    pelicula_3 = peliculas[2]
    pelicula_4 = peliculas[3]
    contador_1 = 0 #Contador de veces que se compra la primera pelicula
    contador_2 = 0
    contador_3 = 0
    contador_4 = 0
    for cliente in clientes: #Verifica en la lista de clientes las peliculas vendidas a cada uno
        if cliente.peli == pelicula_1.titulo: #Si la pelicula del cliente es igual a la pelicula 1 se suma 1 al contador
            contador_1 += 1
        elif cliente.peli == pelicula_2.titulo:
            contador_2 += 1
        elif cliente.peli == pelicula_3.titulo:
            contador_3 += 1
        elif cliente.peli == pelicula_4.titulo:
            contador_4 += 1
    contadores[contador_1] = pelicula_1.titulo #Se agrega al diccionario el contador como key y la pelicula correspondiente como value
    contadores[contador_2] = pelicula_2.titulo
    contadores[contador_3] = pelicula_3.titulo
    contadores[contador_4] = pelicula_4.titulo
    for w, (x, y) in enumerate(contadores.items(),1):
        print("Pelicula: ",w,"Nombre: ",y,"Comprada: ",x,"veces")

def contador_clientes():
    """
    Contador de clientes fieles
    """
    cedulas = [] #Lista de cedulas
    nombres = {} #Diccionario de cedulas como keys y el nombre correspondiente como value
    for cliente in list(set(clientes)):
        nombres[cliente.cedula] = cliente.nombre
    for cliente in clientes:
        cedulas.append(cliente.cedula)
    clientes_ord = sorted(cedulas)
    cedulas_ord = sorted(list(set(cedulas)))
    contador_clientes = []
    j = 0
    while j < len(clientes_ord):
        contador = 0
        t = clientes_ord.count(clientes_ord[j])
        contador += t
        j += t
        contador_clientes.append(contador)
        if j >= len(clientes_ord):
            break
    y = contador_clientes.index(max(contador_clientes))
    print("Cliente más fiel: {}, cédula: {}".format(nombres.get(cedulas_ord[y]),cedulas_ord[y]))
    contador_clientes.pop(y)
    y = contador_clientes.index(max(contador_clientes))
    print("Segundo cliente más fiel: {}, cédula: {}".format(nombres.get(cedulas_ord[y]),cedulas_ord[y]))
    contador_clientes.pop(y)
    y = contador_clientes.index(max(contador_clientes))
    print("Tercer cliente más fiel: {}, cédula: {}".format(nombres.get(cedulas_ord[y]),cedulas_ord[y]))
            
def contador_productos():
    """
    Contador de productos más vendidos
    """
    chucherias_ord = sorted(chucherias_compradas)
    nombre_c = list(set(chucherias_ord))
    contador_chuches = []
    j = 0
    while j < len(chucherias_ord):
        contador = 0
        t = chucherias_ord.count(chucherias_ord[j])
        contador += t
        j += t
        contador_chuches.append(contador)
        if j >= len(chucherias_ord):
            break
    y = contador_chuches.index(max(contador_chuches))
    print("Producto más comprado: {}. {} veces".format(nombre_c[y], contador_chuches[y]))
    contador_chuches.pop(y)
    y = contador_chuches.index(max(contador_chuches))
    print("Segundo producto más comprado: {}. {} veces".format(nombre_c[y], contador_chuches[y]))
    contador_chuches.pop(y)
    y = contador_chuches.index(max(contador_chuches))
    print("Tercer producto más comprado: {}. {} veces".format(nombre_c[y], contador_chuches[y]))
    contador_chuches.pop(y)
    y = contador_chuches.index(max(contador_chuches))
    print("Cuarto producto más comprado: {}. {} veces".format(nombre_c[y], contador_chuches[y]))
    contador_chuches.pop(y)
    y = contador_chuches.index(max(contador_chuches))
    print("Quinto producto más comprado: {}. {} veces".format(nombre_c[y], contador_chuches[y]))

#BASE DE DATOS
def archivo_peliculas():
    """
    Funcion para crear la base de datos de peliculas
    """
    with open("base_de_datos_peliculas.txt","a") as f: 
        #Se abre o se crea (Si no existe) el archivo de base de datos en modo "append" para agregar y no sobreescribir los nuevos datos
        f.write("Peliculas: ---------------------------------------------------\n")
        for pelicula in peliculas:
            f.write("Titulo ")
            f.write(pelicula.titulo) #Se escribe en una linea nueva del txt cada pelicula
            f.write("\n")
            f.write("Sala ")
            f.write(pelicula.sala)
            f.write("\n")
            f.write("Director ")
            f.write(pelicula.director)
            f.write("\n")
            f.write("Rating ")
            f.write(str(pelicula.imdb))
            f.write("\n")
            f.write("Clasificacion ")
            f.write(pelicula.clasificacion)
            f.write("\n")
            f.write("Genero ")
            f.write(pelicula.genero)
            f.write("\n")
            f.write("Reparto ")
            for actor in pelicula.reparto:
                f.write(actor)
                f.write("\n")
            f.write("\n")

def archivo_clientes():
    """
    Funcion para crear la base de datos de clientes
    """
    with open("base_de_datos_clientes.txt","a") as b:
        b.write("Clientes: ---------------------------------------------\n")
        if len(clientes) > 0:
            for cliente in clientes:
                b.write("Nombre ")
                b.write(cliente.nombre)
                b.write("\n")
                b.write("Cedula ")
                b.write(cliente.cedula)
                b.write("\n")
                b.write("Edad ")
                b.write(str(cliente.edad))
                b.write("\n")
                b.write("Pelicula comprada ")
                b.write(cliente.peli)
                b.write("\n")
        else:
            b.write("No hubo clientes")

def archivo_productos():
    """
    Funcion para crear la base de datos de productos y combos
    """
    with open("base_de_datos_productos.txt","a") as p:
        p.write("Productos y combos: --------------------------------------------\n")
        for producto in productos:
            p.write("Nombre ")
            p.write(producto.nombre)
            p.write("\n")
            p.write("Tipo ")
            p.write(producto.tipo)
            p.write("\n")
            p.write(producto.caracteristica)
            p.write("\n")
            p.write("Precio ")
            p.write(str(producto.precio))
            p.write("\n")
        for combo in combos:
            p.write("Nombre del combo ")
            p.write(combo.nombre_combo)
            p.write("\n")
            p.write("Precio ")
            p.write(str(combo.monto))
            p.write("\n")
            p.write("Productos ")
            for producto in combo.productos:
                p.write(producto)
                p.write("\n")
            p.write("\n")   

def main():
    """
    Funcion main para llamar al resto de funciones.
    Se hace un menu para tener las diferentes opciones
    """
    indice = 0
    i_c = 0
    ind_cost = 0
    while True:
        print("-"*60)
        menu_general = input(
            "Seleccione una opcion: \n1. Gestión de películas \n2. Gestión de productos \n3. Gestión de combos \n4. Buscar película \n5. Comprar ticket \n6. Salir \n"
        ) #Menu general del cine. Se puede acceder a todos los módulos
        print("-"*60)
        if menu_general == "1":
            while True: #While loop para crear cada pelicula
                menu_peliculas = input("Que desea hacer: \n1. Agregar pelicula a la cartelera \n2. Modificar película de la cartelera \n3. Eliminar película de la cartelera \n4. Ver cartelera \n5. Salir \n")
                if menu_peliculas == "1":
                    print("Creacion de peliculas:")
                    peliculas.append(crear_pelicula())
                    print("-"*60)
                elif menu_peliculas == "2":
                    if len(peliculas) > 0:
                        for pelicula in peliculas:
                            print("-"*60)
                            pelicula.descripcion_pelicula() #Descripcion de cada pelicula
                            print("-"*60)
                        modificacion = int(input("Seleccione la peicula que va a modificar según su posicion en la cartelera: "))
                        s = peliculas[modificacion - 1]
                        salas.append(s.sala)
                        peliculas.pop(modificacion - 1) #Se elimina la pelicula que se escoge
                        peliculas.append(crear_pelicula()) #se agrega la pelicula modificada
                    else: 
                        print("No hay películas en cartelera todavía")
                elif menu_peliculas == "3":
                    if len(peliculas) > 0:
                        for pelicula in peliculas:
                            print("-"*60)
                            pelicula.descripcion_pelicula() 
                            print("-"*60)
                        eliminar = int(input("Seleccione a pelicula que desea eliminar de la cartelera según su posición: "))
                        s = peliculas[eliminar - 1]
                        salas.append(s.sala)
                        peliculas.pop(eliminar - 1) #Se elimina la pelicula segun la posicion que se escriba en el input
                    else:
                        print("No hay películas en cartelera todavía")
                elif menu_peliculas == "4":
                    for pelicula in peliculas:
                        print("-"*60)
                        pelicula.descripcion_pelicula()
                        print("-"*60)
                elif menu_peliculas == "5":
                    break
                else: 
                    print("Seleccione una opcion válida")
                if len(peliculas) < 4: 
                    mas_peliculas = input("Desea salir o seguir gestionando películas? (Escriba salir o seguir) ").lower()
                    if mas_peliculas == "salir":
                        break
                elif len(peliculas) > 4:
                    print("Usted ha excedido la cantidad de peliculas en cartelera. A continuacion se eliminará la ultima que agregó")
                    peliculas.pop(4)
                elif len(peliculas) == 4: #Cantidad máxima de películas en cartelera
                    salir = input("Ya se ha alcanzado la cantidad máxima de peliculas en la cartelera. Desea Salir? (Si o No) ").lower()
                    if salir == "si" or salir == "salir" or salir == "s":
                        break #Rompe el loop y termina de crearse la carteleras
                #Pelicula creada y agregada a la lista
        elif menu_general == "2":
            while True: #While loop para crear los productos que se venden en la caramelería
                menu_productos = input("Que desea hacer: \n1. Agregar producto \n2. Modificar producto \n3. Eliminar producto \n4. Ver productos \n5. Salir\n")
                if menu_productos == "1":
                    productos.append(crear_producto())
                elif menu_productos == "2":
                    if len(productos) > 0:
                        for producto in productos:
                            print("-"*60)
                            producto.descrip_producto()
                            print("-"*60)
                        modificar = int(input("Seleccione el producto que quiere modificar según su posición en el menú: "))
                        productos.pop(modificar - 1) #Se elimina el producto que se elige
                        productos.append(crear_producto()) #Se vuelve a agregar el producto modificado en la lista
                    else:
                        print("No hay productos en el en menu")
                elif menu_productos == "3":
                    if len(productos) > 0:
                        for prodcto in productos:
                            print("-"*60)
                            prodcto.descrip_producto()
                            print("-"*60)
                        borrar = int(input("Seleccione el producto que quiera eliminar del menú según su posición: "))
                        productos.pop(borrar - 1) #Se elimina el producto 
                    else:
                        print("No hay productos en el en menu")
                elif menu_productos == "4":
                    for producto in productos:
                        print("-"*60)
                        producto.descrip_producto()
                        print("-"*60)
                elif menu_productos == "5":
                    break
                else:
                    print("Seleccione una opción válida")
                seguir = input("Desea agregar, modificar, eliminar o ver los productos? (Si o No) ").title() #Para seguir agregando productos al menú
                if seguir == "N" or seguir == "No":
                    break 
            #Producto creado y agregado a la lista de productos
        elif menu_general == "3":
            while True: #While loop para crear los combos
                menu_combos = input("Que desea hacer: \n1. Agregar combo \n2. Modificar combo \n3. Eliminar combo \n4. Ver combos \n5. Salir \n")
                if menu_combos == "1":
                    combos.append(crear_combo())
                elif menu_combos == "2":
                    if len(combos) > 0:
                        for combo in combos:
                            print("-"*60)
                            combo.descrip_combo()
                            print("-"*60)
                        modificar_combo = int(input("Seleccione el combo que quiere modificar según su posición en el menú: "))
                        combos.pop(modificar_combo - 1) #Se elimina el combo que se escogio
                        combos.append(crear_combo()) #Se vuelve a agregar el combo ya modificado
                    else:
                        print("No hay combos en el en menu")
                elif menu_combos == "3":
                    if len(combos) > 0:
                        for combo in combos:
                            print("-"*60)
                            combo.descrip_combo()
                            print("-"*60)
                        borrar_combo = int(input("Seleccione el combo que quiera eliminar del menú según su posición: "))
                        combos.pop(borrar_combo - 1) #Se elimina el combo que se escogió
                    else:
                        print("No hay combos en el en menu")
                elif menu_combos == "4":
                    for combo in combos:
                        print("-"*60)
                        combo.descrip_combo()
                        print("-"*60)
                elif menu_combos == "5":
                    break
                else:
                    print("Seleccione una opción válida")
                seguir2 = input("Desea agregar, modificar, eliminar o ver los combos? (Si o No) ").title() #Para seguir agregando combos al menú
                if seguir2 == "N" or seguir2 == "No":
                    break 
            #Combo creado y agregado a la lista
            #Compra de tickets
        elif menu_general == "4":
            filtro_pelicula()
        elif menu_general == "5":
            if len(peliculas) > 0:
                while True: #While loop para comprar el ticket
                    print("Bienvenido a Cine Saman")
                    comprar = input("Desea comprar un ticket? (Si o No) ").lower()
                    if comprar == "n" or comprar == "no":
                        break
                    filtro_pelicula()
                    clientes.append(crear_cliente())
                    while indice < len(clientes):
                        costo = 0.0   
                        precio_carameleria = 0.0
                        chucherias_compradas2 = [] #Lista de chucherias compradas para despues imprimirlas en el resumen de compra del cliente
                        cliente = clientes[indice] #Usa la variable indice para asignar el valor que tiene la variable cliente
                        asiento = cliente.asiento
                        if cliente.edad <= 18: #Chequea la edad del cliente
                            costo = 10.0 #Costo de la entrada según la edad
                            cedula = cliente.cedula
                            edad = cliente.edad
                            if capicua(cedula):
                                print("Felicidades! Tiene un descuento de 11%")
                                costo -= costo * 0.11
                            if num_primo(edad):
                                print("Felicidades! Tienes un descuento de 7%")
                                costo -= costo * 0.07
                            print("El costo de su entrada es de:",costo,"Bs")
                            costos.append(costo)
                        elif cliente.edad < 60 and cliente.edad > 18:
                            costo = 15.0
                            cedula = cliente.cedula
                            edad = cliente.edad
                            if capicua(cedula):
                                print("Felicidades! Tiene un descuento de 11%")
                                costo -= costo * 0.11
                            if num_primo(edad):
                                print("Felicidades! Tienes un descuento de 7%")
                                costo -= costo * 0.07
                            print("El costo de su entrada es de:",costo,"Bs")
                            costos.append(costo)
                        elif cliente.edad >= 60:
                            costo = 12.0
                            cedula = cliente.cedula
                            edad = cliente.edad
                            if capicua(cedula):
                                print("Felicidades! Tiene un descuento de 11%")
                                costo -= costo * 0.11
                            if num_primo(edad):
                                print("Felicidades! Tienes un descuento de 7%")
                                costo -= costo * 0.07
                            print("El costo de su entrada es de:",costo,"Bs")
                            costos.append(costo)
                        compra_carameleria = input("Desea comprar algo en la caramelería? (Si o No) ").lower() 
                        #Variable para que el cliente compre en la carameleria. Si no quiere se pregunta si procedera con la compra
                        if (compra_carameleria == "s" or compra_carameleria == "si") and (len(productos) >= 1 or len(combos) >= 1):
                            while True:
                                compra = input("Desea un combo o una chucheria sola? ").lower()
                                if compra == "chucheria" or compra == "chucheria sola":
                                    filtro_producto() #Se llama la funcion de filtro de productos
                                    compra2 = input("Escriba el nombre de la chucheria que quiere comprar: ").title()
                                    chucherias_compradas2.append(compra2)
                                    chucherias_compradas.append(compra2)
                                    #Se agrega un sub lista de chucherías compradas por cliente a la lista general de chucherías compradas
                                    for producto in productos:
                                        if producto.nombre == compra2: #Revisa que el producto esté en venta
                                            precio = producto.precio
                                            iva(precio)
                                            precio_carameleria += precio
                                            print("Precio a pagar:",producto.precio,"Bs")
                                elif compra == "combo":  
                                    filtro_combo() #Se llama la funcion de busqueda de combos 
                                    compra2 = input("Escriba el nombre del combo que quiere comprar: ").title()
                                    chucherias_compradas2.append(compra2)
                                    for combo in combos:
                                        if combo.nombre_combo == compra2: #Revisa que el combo este entre los que se ofrecen
                                            precio = combo.monto
                                            iva(precio)
                                            precio_carameleria += precio
                                            print("Precio a pagar:",combo.monto,"Bs")
                                compra3 = input("Quiere comprar alguna otra cosa? (Si o No) ")
                                if compra3 == "n" or compra2 == "no":
                                    break 
                            costos_carameleria.append(precio_carameleria) 
                            #Se agrega el gasto que hizo el cliente a la lista general de los gastos en caramelería para despues usarlo en las estadisticas
                            precio_total = costo + precio_carameleria #Precio total que tiene que pagar el cliente
                            if precio_total > precio_carameleria:
                                print("Felicidades! Tienes un descuento de 10%")
                                precio_total -= precio_total * 0.1 
                                #descuento si el precio total a pagar del cliente es mayor a la suma de todos los precios de la carameleria
                            elif precio_total < abundante(precio_total):
                                print("Felicidades! Tiene un descuento de 15%")
                                precio_total -= precio_total * 0.15
                                #descuento si el precio total es un numero abundante
                            print("-"*30)
                            cliente.descrip_cliente()
                            print("Monto a pagar: ",precio_total,"Bs")
                            print("Productos o combos comprados:")
                            for chucheria in chucherias_compradas2:
                                print("     ",chucheria)
                            print("-"*30)
                            confirmar = input("Desea proceder con su compra? (Si o No) ").lower()
                            if confirmar == "no" or confirmar == "n":
                                costos.pop(indice) #Quita el último costo agregado, que sería el del cliente actual
                                costos_carameleria.pop(ind_cost) #Quita el último costo de la caramelería agregado, que sería el del cliente actual usando el indice de costo (ind_cost)
                                ind_cost -= 1
                                for x in range(len(chucherias_compradas2)):    
                                    chucherias_compradas.pop(i_c + x - 1) # quita las chucherias agregadas a la lista general segun el indice de carameleria (i_c) y le suma 1 por cada chucheria que haya en la lista de chucherias por cliente
                                i_c -= 1
                                for pelicula in peliculas: 
                                    if pelicula.titulo == cliente.peli:
                                        pelicula2 = pelicula.sala #define la película que va a ver el cliente como pelicula2 y como el objeto de pelicula correspondiente para poder usar sus atributos
                                i = 0
                                while i < 6:
                                    if pelicula2 == "2D":
                                        hileras = sala1[i]
                                        if True:
                                            if "A" in asiento:
                                                i = 0
                                            elif "B" in asiento:
                                                i = 1
                                            elif "C" in asiento:
                                                i = 2
                                            elif "D" in asiento:
                                                i = 3
                                            elif "E" in asiento:
                                                i = 4
                                        if ("A" in asiento or "B" in asiento or "C" in asiento or "D" in asiento or "E" in asiento) and "XX" in hileras:
                                            #Verifica que haya una letra  
                                            if "1" in asiento:
                                                hileras[u] = asiento
                                            elif "2" in asiento:
                                                hileras[v] = asiento
                                            elif "3" in asiento:
                                                hileras[w] = asiento
                                            elif "4" in asiento:
                                                hileras[x] = asiento
                                            elif "5" in asiento:
                                                hileras[y] = asiento
                                            break
                                    elif pelicula2 == "3D":
                                        hileras = sala2[i]
                                        if True:
                                            if "A" in asiento:
                                                i = 0
                                            elif "B" in asiento:
                                                i = 1
                                            elif "C" in asiento:
                                                i = 2
                                            elif "D" in asiento:
                                                i = 3
                                            elif "E" in asiento:
                                                i = 4
                                            elif "F" in asiento:
                                                i = 5
                                        if ("A" in asiento or "B" in asiento or "C" in asiento or "D" in asiento or "E" in asiento or "F" in asiento) and "XX" in hileras:
                                            if "1" in asiento:
                                                hileras[u] = asiento
                                            elif "2" in asiento:
                                                hileras[v] = asiento
                                            elif "3" in asiento:
                                                hileras[w] = asiento
                                            elif "4" in asiento:
                                                hileras[x] = asiento
                                            elif "5" in asiento:
                                                hileras[y] = asiento
                                            elif "6" in asiento:
                                                hileras[z] = asiento
                                            break
                                    elif pelicula2 == "4DX":
                                        hileras = sala3[i]
                                        if True:
                                            if "A" in asiento:
                                                i = 0
                                            elif "B" in asiento:
                                                i = 1
                                            elif "C" in asiento:
                                                i = 2
                                            elif "D" in asiento:
                                                i = 3
                                        if ("A" in asiento or "B" in asiento or "C" in asiento or "D" in asiento) and "XX" in hileras:
                                            if "1" in asiento:
                                                hileras[u] = asiento
                                            elif "2" in asiento:
                                                hileras[v] = asiento
                                            elif "3" in asiento:
                                                hileras[w] = asiento
                                            elif "4" in asiento:
                                                hileras[x] = asiento
                                            break
                                    elif pelicula2 == "VIP":
                                        hileras = sala4[i]
                                        if True:
                                            if "A" in asiento:
                                                i = 0
                                            elif "B" in asiento:
                                                i = 1
                                            elif "C" in asiento:
                                                i = 2
                                        if ("A" in asiento or "B" in asiento or "C" in asiento) and "XX" in hileras:
                                            if "1" in asiento:
                                                hileras[u] = asiento
                                            elif "2" in asiento:
                                                hileras[v] = asiento
                                            elif "3" in asiento:
                                                hileras[w] = asiento
                                            break
                                clientes.pop(indice)
                            break
                        else:
                            print("En este momento no hay productos ni combos en la caramelería")
                            i_c -= 1
                            ind_cost -= 1
                            print("-"*30)
                            cliente.descrip_cliente()
                            print(costo,"Bs") #Se usa costo y no precio total porque solo se paga la entrada
                            print("Productos o combos comprados: \n Ninguno")
                            print("-"*30)
                            confirmar = input("Desea proceder con su compra? (Si o No) ").lower()
                            if confirmar == "no" or confirmar == "n":
                                costos.pop(indice) #Quita el último costo agregado, que sería el del cliente actual
                                for pelicula in peliculas: 
                                    if pelicula.titulo == cliente.peli:
                                        pelicula2 = pelicula.sala #define la película que va a ver el cliente como pelicula2 y como el objeto de pelicula correspondiente para poder usar sus atributos
                                i = 0
                                while i < 6:
                                    if pelicula2 == "2D":
                                        hileras = sala1[i]
                                        if True: #Verifica la letra del asiento para ubicar la fila de asientos en la que está
                                            if "A" in asiento:
                                                i = 0
                                            elif "B" in asiento:
                                                i = 1
                                            elif "C" in asiento:
                                                i = 2
                                            elif "D" in asiento:
                                                i = 3
                                            elif "E" in asiento:
                                                i = 4
                                        if ("A" in asiento or "B" in asiento or "C" in asiento or "D" in asiento or "E" in asiento) and "XX" in hileras: 
                                            #Verifica que haya una de las letras y que "XX" esté en la fila
                                            if "1" in asiento: #Verifica el número que tiene el asiento para ubicarse en la columna
                                                hileras[u] = asiento #Convierte el "XX" en el asiento
                                            elif "2" in asiento:
                                                hileras[v] = asiento
                                            elif "3" in asiento:
                                                hileras[w] = asiento
                                            elif "4" in asiento:
                                                hileras[x] = asiento
                                            elif "5" in asiento:
                                                hileras[y] = asiento
                                            break
                                    elif pelicula2 == "3D":
                                        hileras = sala2[i]
                                        if True:
                                            if "A" in asiento:
                                                i = 0
                                            elif "B" in asiento:
                                                i = 1
                                            elif "C" in asiento:
                                                i = 2
                                            elif "D" in asiento:
                                                i = 3
                                            elif "E" in asiento:
                                                i = 4
                                            elif "F" in asiento:
                                                i = 5
                                        if ("A" in asiento or "B" in asiento or "C" in asiento or "D" in asiento or "E" in asiento or "F" in asiento) and "XX" in hileras:
                                            if "1" in asiento:
                                                hileras[u] = asiento
                                            elif "2" in asiento:
                                                hileras[v] = asiento
                                            elif "3" in asiento:
                                                hileras[w] = asiento
                                            elif "4" in asiento:
                                                hileras[x] = asiento
                                            elif "5" in asiento:
                                                hileras[y] = asiento
                                            elif "6" in asiento:
                                                hileras[z] = asiento
                                            break
                                    elif pelicula2 == "4DX":
                                        hileras = sala3[i]
                                        if True:
                                            if "A" in asiento:
                                                i = 0
                                            elif "B" in asiento:
                                                i = 1
                                            elif "C" in asiento:
                                                i = 2
                                            elif "D" in asiento:
                                                i = 3
                                        if ("A" in asiento or "B" in asiento or "C" in asiento or "D" in asiento) and "XX" in hileras:
                                            if "1" in asiento:
                                                hileras[u] = asiento
                                            elif "2" in asiento:
                                                hileras[v] = asiento
                                            elif "3" in asiento:
                                                hileras[w] = asiento
                                            elif "4" in asiento:
                                                hileras[x] = asiento
                                            break
                                    elif pelicula2 == "VIP":
                                        hileras = sala4[i]
                                        if True:
                                            if "A" in asiento:
                                                i = 0
                                            elif "B" in asiento:
                                                i = 1
                                            elif "C" in asiento:
                                                i = 2
                                        if ("A" in asiento or "B" in asiento or "C" in asiento) and "XX" in hileras:
                                            if "1" in asiento:
                                                hileras[u] = asiento
                                            elif "2" in asiento:
                                                hileras[v] = asiento
                                            elif "3" in asiento:
                                                hileras[w] = asiento
                                            break
                                clientes.pop(indice)
                            break
                    proximo = input("Siguiente cliente? (Si o No) ").lower() 
                    #Pregunta si hay otro cliente. Si no hay se rompe el loop
                    if proximo == "no" or proximo == "n":
                        i_c += 1
                        ind_cost += 1
                        indice += 1 
                        break
                    else: #Si hay otro cliente se le suma 1 al indice y empieza la compra del siguiente cliente
                        i_c += 1
                        ind_cost += 1
                        indice += 1
            elif len(peliculas) == 0:
                print("No hay películas en cartelera en este momento")
        elif menu_general == "6":
            if len(peliculas) < 4:
                print("No se puede salir porque no se ha completado la cartelera") 
            elif len(clientes) == 0:
                salir = input("Todavía no se han comprado tickets. Seguro que quieres salir? (Si o No)").lower()
                if salir == "si" or salir == "s":
                    break
            else:
                salir = input("Seguro que quieres salir? (Si o No) ").lower()
                if salir == "si" or salir == "s":
                    break
    todos_clientes = input("Desea ver los datos de todos los clientes? (Si o No) ").lower()
    if todos_clientes == "s" or todos_clientes == "si": 
        #si se quiere ver a todos los clientes se hace un for que imprima cada uno con sus datos
        for cliente in clientes:
            print("-"*60)
            cliente.descrip_cliente()
            print("-"*60)
    while True:
        if len(clientes) > 0:
            print("-"*60)
            menu_estadistica = input(
                "Seleccione una de las opciones: \n1. Promedio de gasto en el cine \n2. Porcentaje de clientes que no compran en caramelería \n3. Peliculas más taquilleras \n4. Clientes más fieles \n5. Productos más vendidos \n6. Salir \n"
            )
            print("-"*60)
            if menu_estadistica == "1":    
                print("Promedio de gasto de los clientes ",prom_gasto())
            elif menu_estadistica == "2":
                print("Porcentaje de clientes que no compran caramelería ",no_carameleria(),"%")
            elif menu_estadistica == "3":
                contador_peliculas()
            elif menu_estadistica == "4":
                contador_clientes()
            elif menu_estadistica == "5":
                contador_productos()
            elif menu_estadistica == "6":
                salir2 = input("Seguro que quiere salir? (Si o No) ").lower()
                if salir2 == "si" or salir2 == "s":
                    break
        else:
            print("No se pueden mostrar las estadísticas porque no hay clientes")
    archivo_peliculas()
    archivo_clientes()
    archivo_productos()

main()        