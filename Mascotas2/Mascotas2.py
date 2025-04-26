"""
Título de práctica:  mascotas2

Extensión del sistema de registro de mascotas con visualización de resumen usando herencia múltiple.

Autor: Luis Felipe Cardozo Herrada <luisfecardozoherrada@gmail.com>
Fecha: 2025-04-25
"""

import datetime
from typing import List, Union

class Visualizador:
    """
    Clase base para visualización de objetos. 
    Contiene el método resumen que retorna la representación formateada del objeto.
    """

    def resumen(self) -> str:
        """
        Devuelve un resumen en formato de tabla de la mascota.
        """
        return f"|{self.__class__.__bases__[0].__name__:5} |{self.nombre:8} |{self.edad} años |{self.raza.title():13} |{self.fecha_ingreso.isoformat():25} |"


class Mascota:
    """
    Clase base que representa una mascota en la veterinaria.
    """

    def __init__(self, nombre: str, edad: int, raza: str):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.datetime.now()
    
    def obtener_tipo(self) -> str:
        """Devuelve el tipo de mascota (nombre de la clase)."""
        return self.__class__.__name__


class Perro(Mascota, Visualizador):
    """Clase que representa un perro, con funcionalidad de visualización."""
    pass


class Gato(Mascota, Visualizador):
    """Clase que representa un gato, con funcionalidad de visualización."""
    pass


def ingresar_mascota(numero: int) -> Union[Perro, Gato]:
    while True:
        tipo = input(f"> Mascota {numero}, que clase es (P)erro o (G)ato?\n< ").strip().lower()
        if tipo in ['perro', 'p']:
            clase = Perro
            tipo_str = "Perro"
            break
        elif tipo in ['gato', 'g']:
            clase = Gato
            tipo_str = "Gato"
            break
        else:
            print("> Por favor ingrese solo 'Perro' o 'Gato'")
    
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
    print("\n> Resumen:")
    print("> |Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    for mascota in mascotas:
        print("> " + mascota.resumen())


def test_unitario() -> None:
    """Prueba unitaria del sistema básico de mascotas."""
    test_perro = Perro("Rex", 2, "Bulldog")
    test_gato = Gato("Michi", 3, "Persa")
    
    assert test_perro.nombre == "Rex"
    assert test_gato.edad == 3
    assert isinstance(test_perro.fecha_ingreso, datetime.datetime)
    assert "Rex" in test_perro.resumen()
    assert "Michi" in test_gato.resumen()
    
    print("Test unitario pasado con éxito!")


def main() -> None:
    test_unitario()
    
    print("Bienvenido al sistema de registro de mascotas de la veterinaria\n")
    
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
    for i in range(1, cantidad + 1):
        mascota = ingresar_mascota(i)
        mascotas.append(mascota)
    
    mostrar_resumen(mascotas)


if __name__ == "__main__":
    main()
