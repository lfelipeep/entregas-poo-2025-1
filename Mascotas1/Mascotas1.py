"""
Título de práctica:  mascotas1

creacion de registro de mascotas con fecha de registro

Autor: Luis Felipe Cardozo Herrada <luisfecardozoherrada@gmail.com>
Fecha: 2025-03-28
"""

import datetime
from typing import List, Union

class Mascota:
    """
    Clase base que representa una mascota en la veterinaria.
    
    Atributos:
        nombre (str): Nombre de la mascota
        edad (int): Edad en años de la mascota
        raza (str): Raza de la mascota
        fecha_ingreso (datetime): Fecha y hora de ingreso a la veterinaria
    """
    
    def __init__(self, nombre: str, edad: int, raza: str):
        """
        Inicializa una nueva mascota con los datos básicos.
        
        
            nombre: Nombre de la mascota
            edad: Edad en años
            raza: Raza de la mascota
        """
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.datetime.now()
    
    def __str__(self) -> str:
        """Devuelve una representación en string de la mascota."""
        return f"|{self.__class__.__name__:5} |{self.nombre:8} |{self.edad:5} |{self.raza:13} |{self.fecha_ingreso.isoformat():25} |"
    
    def obtener_tipo(self) -> str:
        """Devuelve el tipo de mascota (nombre de la clase)."""
        return self.__class__.__name__


class Perro(Mascota):
    """Clase que representa un perro, derivada de Mascota."""
    pass


class Gato(Mascota):
    """Clase que representa un gato, derivada de Mascota."""
    pass


def ingresar_mascota(numero: int) -> Union[Perro, Gato]:
    """
    Función para ingresar los datos de una mascota por consola.
    
    
        numero: Número de mascota que se está ingresando
        
    Returns:
        Instancia de Perro o Gato con los datos ingresados
    """
    while True:
        tipo = input(f"> Mascota {numero}, que clase es Perro o Gato?\n< ").lower()
        if tipo in [  'perro']:
            clase = Perro
            tipo_str = "Perro"
            break
        elif tipo in [ 'gato']:
            clase = Gato
            tipo_str = "Gato"
            break
        else:
            print("> Por favor ingrese nomas Perro o  Gato")
    
    nombre = input(f"> cual es el nombre del {tipo_str}?\n< ").strip()
    while not nombre:
        print("> El nombre no puede estar vacío")
        nombre = input(f"> cual es el nombre del {tipo_str}?\n< ").strip()
    
    while True:
        edad_str = input(f"> que edad tiene '{nombre}'?\n< ").strip()
        try:
            edad = int(edad_str)
            if edad <= 0:
                print("> La edad debe ser un número positivo")
            else:
                break
        except ValueError:
            print("> Por favor ingrese un número válido para la edad")
    
    raza = input(f"> de que raza es '{nombre}'?\n< ").strip()
    while not raza:
        print("> La raza no puede estar vacía")
        raza = input(f"> de que raza es '{nombre}'?\n< ").strip()
    
    return clase(nombre, edad, raza)


def mostrar_resumen(mascotas: List[Union[Perro, Gato]]) -> None:
    """
    Muestra un resumen tabular de todas las mascotas ingresadas.
    
    
        mascotas: Lista de instancias de mascotas a mostrar
    """
    print("\n> Resumen:")
    print("> |Clase |Nombre   |Edad |Raza         |Fecha de ingreso          |")
    for mascota in mascotas:
        print("> " + str(mascota))


def test_unitario() -> None:
    """Función de test unitario para verificar el funcionamiento básico."""
    # Crear una mascota de prueba
    test_mascota = Perro("Test", 5, "Labrador")
    
    # Verificar los atributos
    assert test_mascota.nombre == "Test"
    assert test_mascota.edad == 5
    assert test_mascota.raza == "Labrador"
    assert isinstance(test_mascota.fecha_ingreso, datetime.datetime)
    assert test_mascota.obtener_tipo() == "Perro"
    
    print("Test unitario pasado con éxito!")


def main() -> None:
    """Función principal del programa."""
    # Ejecutar test unitario
    test_unitario()
    
    print("Bienvenido al sistema de registro de mascotas de la veterinaria\n")
    
    # Solicitar cantidad de mascotas
    while True:
        try:
            cantidad = int(input("> Cuantas mascotas va a ingresar?\n< "))
            if cantidad <= 0:
                print("> Por favor ingrese un número positivo")
            else:
                break
        except ValueError:
            print("> Por favor ingrese un número válido")
    
    mascotas = []
    
    # Ingresar cada mascota
    for i in range(1, cantidad + 1):
        mascota = ingresar_mascota(i)
        mascotas.append(mascota)
    
    # Mostrar resumen
    mostrar_resumen(mascotas)


if __name__ == "__main__":
    main()