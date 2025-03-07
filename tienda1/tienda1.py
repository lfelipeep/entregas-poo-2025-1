#!/usr/bin/env python3

"""
Título de práctica:  Inventario en Tienda

manejo del invetario de la tienda

Autor: Luis Felipe Cardozo Herrada <luisfecardozoherrada@gmail.com>
Fecha: 2025-02-27
"""


import unittest

class Producto:
   
    def __init__(self, nombre: str, precio: int, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"|{self.nombre:<10}|{self.cantidad:>4} unidades |{self.precio:>6} pesos |"


def solicitar_producto(num):
    """Solicita al usuario los datos de un producto y devuelve una instancia de Producto."""
    nombre = input(f"Producto {num}, ¿cuál es el nombre?\n> ")
    precio = int(input(f"¿Cuál es el precio de '{nombre}'?\n> "))
    cantidad = int(input(f"¿Qué cantidad hay de '{nombre}'?\n> "))
    return Producto(nombre, precio, cantidad)


def run():
    """Script entrypoint"""
    print("Bienvenido al sistema de inventario de la tienda.")
    productos = [solicitar_producto(i) for i in range(1, 4)]

    print("\nResumen:")
    print("|Producto  |Cantidad     |Precio     |")
    print("|----------|------------|-----------|")
    for producto in productos:
        print(producto)


# Test unitario
class TestProducto(unittest.TestCase):
    def test_creacion_producto(self):
        producto = Producto("arroz", 2500, 20)
        self.assertEqual(producto.nombre, "arroz")
        self.assertEqual(producto.precio, 2500)
        self.assertEqual(producto.cantidad, 20)


# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
    unittest.main(exit=False)

