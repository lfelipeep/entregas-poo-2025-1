"""
Título de práctica:  Inventario en Tienda3

Extensión del manejo del inventario de la tienda con nuevas funcionalidades.

Autor: Luis Felipe Cardozo Herrada <luisfecardozoherrada@gmail.com>
Fecha: 2025-03-13
"""


class Producto:
    """Clase que representa un producto en la tienda."""

    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        """
        Inicializa un producto con sus atributos básicos.
        
        :param nombre: Nombre del producto.
        :param precio: Precio unitario del producto.
        :param cantidad: Cantidad disponible en inventario.
        :param descripcion: Breve descripción del producto.
        :param clasificacion: Categoría o clasificación del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def calcula_precio(self, cantidad):
        """Devuelve el precio total a pagar por una cantidad dada."""
        return self.precio * cantidad

    def inventario_precio(self):
        """Calcula el valor total del producto en el inventario."""
        return self.precio * self.cantidad

    def __str__(self):
        """Devuelve una representación formateada del producto."""
        return (f"|{self.nombre:<10}|{self.cantidad:<5} unidades |"
                f"{self.precio:<5} pesos |{self.descripcion[:12]:<12}...|"
                f"{self.clasificacion:<12}|{self.inventario_precio():<10} pesos |"
                f"{self.calcula_precio(5):<10} pesos |")


def solicitar_producto(num):
    """
    Solicita los datos de un producto al usuario y lo crea.
    
    :param num: Número del producto en la lista de entrada.
    :return: Instancia de la clase Producto con los datos ingresados.
    """
    print(f"> Producto {num}, ¿cuál es el nombre?")
    nombre = input("< ").strip()
    precio = validar_entero(f"> ¿Cuál es el precio de '{nombre}'?\n< ")
    cantidad = validar_entero(f"> ¿Qué cantidad hay de '{nombre}'?\n< ")
    descripcion = input(f"> Introduzca la descripción de '{nombre}':\n< ").strip()
    clasificacion = input(f"> ¿Qué clasificación tiene '{nombre}'?\n< ").strip()

    return Producto(nombre, precio, cantidad, descripcion, clasificacion)


def validar_entero(mensaje):
    """
    Solicita un número entero positivo al usuario.
    
    :param mensaje: Mensaje a mostrar al usuario.
    :return: Un número entero válido ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: Debe ingresar un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar un número válido.")


def calcular_precio_unitario_por_clasificacion(productos):
    """
    Calcula el precio unitario total por clasificación.
    
    :param productos: Lista de objetos de tipo Producto.
    :return: Diccionario con la clasificación como clave y la suma de los precios unitarios como valor.
    """
    resumen = {}
    for producto in productos:
        if producto.clasificacion in resumen:
            resumen[producto.clasificacion] += producto.precio
        else:
            resumen[producto.clasificacion] = producto.precio
    return resumen


def mostrar_resumen(productos):
    """
    Muestra en pantalla un resumen de los productos ingresados.
    
    :param productos: Lista de objetos de tipo Producto.
    """
    print("\n> Resumen:")
    print("> |Producto   |Cantidad     |Precio     |Descripción  |Clasificación |Total en inventario |Precio x5 unidades |")
    print("-" * 105)
    for producto in productos:
        print(f"> {producto}")
    print("-" * 105)

    precios_por_clasificacion = calcular_precio_unitario_por_clasificacion(productos)
    print("> Precios por clasificación")
    print("> |Clasificación |Precio unitario |")
    print("-" * 35)
    for clasificacion, precio in precios_por_clasificacion.items():
        print(f"> |{clasificacion:<14}|{precio:<10} pesos |")
    print("-" * 35)


def main():
    """Función principal que ejecuta el programa."""
    num_productos = validar_entero("> ¿Cuántos productos va a ingresar?\n< ")
    productos = [solicitar_producto(i + 1) for i in range(num_productos)]
    mostrar_resumen(productos)


if __name__ == "__main__":
    main()
