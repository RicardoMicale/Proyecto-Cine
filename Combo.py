class Combo:

    def __init__(self,nombre_combo,productos,monto):
        self.nombre_combo = nombre_combo
        self.productos = productos
        self.monto = monto

    def descrip_combo(self):
        print("Combo: {} \nProductos en el combo: {} \nPrecio: {}Bs".format(self.nombre_combo,self.productos,self.monto))