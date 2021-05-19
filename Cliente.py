class Cliente:

    def __init__(self,nombre,cedula,edad,peli,asiento):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.peli = peli
        self.asiento = asiento

    def descrip_cliente(self):
        print(
            "Nombre del cliente: {} \nCédula del cliente: {} \nEdad del cliente: {} \nPelicula que va a ver: {} \nAsiento: {}"
            .format(self.nombre,self.cedula,self.edad,self.peli,self.asiento)
            )

