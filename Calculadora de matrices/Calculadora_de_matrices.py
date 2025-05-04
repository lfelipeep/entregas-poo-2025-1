"""
Título de práctica: Calculadora de matrices

Descripción:
Calculadora basica de matrices 2x2 que permite realizar operaciones 
de suma, resta y multiplicación mediante sobrecarga de operadores.

Autor: Luis Felipe Cardozo Herrada <luisfecardozoherrada@gmail.com>
Fecha: 2025-05-04
"""

class Matriz:
    """
    Clase que representa una matriz 2x2 y permite operaciones básicas
    como suma, resta y multiplicación mediante operadores.
    """

    def __init__(self, elementos):
        """
        Inicializa la matriz con una lista de listas (2x2).
        :para elementos: lista de listas con los 4 valores [[a, b], [c, d]]
        """
        if len(elementos) != 2 or any(len(fila) != 2 for fila in elementos):
            raise ValueError("La matriz debe ser de tamaño 2x2.")
        self.elementos = elementos

    def __add__(self, other):
        """Suma de matrices 2x2"""
        return Matriz([
            [self.elementos[i][j] + other.elementos[i][j] for j in range(2)]
            for i in range(2)
        ])

    def __sub__(self, other):
        """Resta de matrices 2x2"""
        return Matriz([
            [self.elementos[i][j] - other.elementos[i][j] for j in range(2)]
            for i in range(2)
        ])

    def __mul__(self, other):
        """Multiplicación de matrices 2x2"""
        a = self.elementos
        b = other.elementos
        resultado = [
            [
                a[0][0] * b[0][j] + a[0][1] * b[1][j] for j in range(2)
            ],
            [
                a[1][0] * b[0][j] + a[1][1] * b[1][j] for j in range(2)
            ]
        ]
        return Matriz(resultado)

    def __str__(self):
        """Representación en string de la matriz"""
        return f"|{self.elementos[0][0]}  {self.elementos[0][1]}|\n|{self.elementos[1][0]}  {self.elementos[1][1]}|"


def leer_matriz(numero):
    """Función auxiliar para leer una matriz 2x2 desde consola"""
    elementos = []
    print(f"> Matriz {numero}:")
    for i in range(2):
        fila = []
        for j in range(2):
            valor = int(input(f"> Matriz {numero}: elemento {i},{j}\n< "))
            fila.append(valor)
        elementos.append(fila)
    return Matriz(elementos)


def main():
    """Función principal del programa"""
    print("=== Calculadora de Matrices 2x2 ===")
    matriz1 = leer_matriz(1)
    matriz2 = leer_matriz(2)

    print("> Matriz 1:")
    print(matriz1)
    print("> Matriz 2:")
    print(matriz2)

    print("> Escriba 1 para suma, \n>         2 para resta, \n>         3 para multiplicación")
    opcion = input("< ")

    if opcion == "1":
        resultado = matriz1 + matriz2
        print("> La suma de las dos matrices es:")
    elif opcion == "2":
        resultado = matriz1 - matriz2
        print("> La resta de las dos matrices es:")
    elif opcion == "3":
        resultado = matriz1 * matriz2
        print("> La multiplicación de las dos matrices es:")
    else:
        print("Opción no válida.")
        return

    print(resultado)


if __name__ == "__main__":
    main()
