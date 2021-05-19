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

print(abundante(12))