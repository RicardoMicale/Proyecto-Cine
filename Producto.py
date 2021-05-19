class Producto:

    def __init__(self,nombre,tipo,caracteristica,precio):
        self.nombre = nombre
        self.tipo = tipo
        self.caracteristica = caracteristica
        self.precio = precio

    def descrip_producto(self):
        print("Producto: {}\n {} {}\n Costo: {}".format(self.nombre,self.tipo,self.caracteristica,self.precio))