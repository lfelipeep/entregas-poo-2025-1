"""
Título de práctica:  Inventario en Tienda2

manejo del invetario de la tienda2

Autor: Luis Felipe Cardozo Herrada <luisfecardozoherrada@gmail.com>
Fecha: 2025-03-6
"""


class Producto:
   

    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def __str__(self):
        return (f"|{self.nombre:<8} |{self.cantidad:<12} unidades  |"
                f"{self.precio:<6} pesos  |{self.descripcion[:12]:<12}...|"
                f"{self.clasificacion:<12} |")


def solicitar_producto(num):
  
    print(f"> Producto {num}, cual es el nombre?")
    nombre = input("< ").strip()
    precio = validar_entero(f"> cual es el precio de '{nombre}'?\n< ")
    cantidad = validar_entero(f"> que cantidad hay de '{nombre}'?\n< ")
    descripcion = input(f"> introduzca la descripción de '{nombre}':\n< ").strip()
    clasificacion = input(f"> qué clasificación tiene '{nombre}'?\n< ").strip()

    return Producto(nombre, precio, cantidad, descripcion, clasificacion)


def validar_entero(mensaje):
  
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: Debe ingresar un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar un número válido.")


def calcular_precio_por_clasificacion(productos):
   
    resumen = {}
    for producto in productos:
        total = producto.precio * producto.cantidad
        if producto.clasificacion in resumen:
            resumen[producto.clasificacion] += total
        else:
            resumen[producto.clasificacion] = total
    return resumen


def mostrar_resumen(productos):
   
    print("\n> Resumen:")
    print("> |Producto |Cantidad     |Precio     |Descripción  |Clasificación |")
    print("-" * 70)
    for producto in productos:
        print(f"> {producto}")
    print("-" * 70)

    precios_por_clasificacion = calcular_precio_por_clasificacion(productos)
    print("> Precios por clasificación")
    print("> |Clasificación |Precio     |")
    print("-" * 30)
    for clasificacion, precio in precios_por_clasificacion.items():
        print(f"> |{clasificacion:<14} |{precio} pesos |")
    print("-" * 30)


def main():
    
    num_productos = validar_entero("> Cuantos productos va a ingresar?\n< ")
    productos = [solicitar_producto(i + 1) for i in range(num_productos)]
    mostrar_resumen(productos)


if __name__ == "__main__":
    main()

