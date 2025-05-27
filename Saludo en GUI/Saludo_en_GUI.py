""" 
Título de práctica: Saludo en GUI

Descripción:
Aplicación gráfica desarrollada con Tkinter que permite ingresar un nombre y recibir un saludo personalizado. La interfaz cuenta con campos de entrada, 
botones interactivos y uso de ventanas emergentes (messagebox). Se aplicaron principios de diseño amigable y pruebas unitarias para validar la funcionalidad.

Autor: Luis Felipe Cardozo Herrada <luisfecardozoherrada@gmail.com>  
Fecha: 2025-05-26
 """

import tkinter as tk
from tkinter import messagebox

class SaludoApp:
    """
    Aplicación gráfica que permite ingresar un nombre y mostrar un saludo personalizado.
    """

    def __init__(self, root):
        """
        Constructor que inicializa la interfaz gráfica.
        :param root: Ventana raíz de Tkinter.
        """
        self.root = root
        self.root.title("Aplicación de Saludo")
        self.root.geometry("300x200")
        self.root.configure(bg="#5A827E")

        # Label que indica el dato a ingresar
        self.label_nombre = tk.Label(root, text="Ingrese su nombre:", bg="#5A827E", font=("Arial", 12))
        self.label_nombre.pack(pady=10)

        # Entry para ingresar el nombre
        self.entry_nombre = tk.Entry(root, width=30)
        self.entry_nombre.pack(pady=5)

        # Botón para mostrar el saludo
        self.boton_saludar = tk.Button(root, text="Saludar", command=self.saludar, bg="#84AE92", fg="white", font=("Arial", 10, "bold"))
        self.boton_saludar.pack(pady=10)

        # Botón para salir del programa
        self.boton_salir = tk.Button(root, text="Salir", command=self.root.quit, bg="black", fg="white", font=("Arial", 10, "bold"))
        self.boton_salir.pack(pady=5)

    def saludar(self):
        """
        Función que obtiene el nombre del Entry y muestra un saludo en una messagebox.
        """
        nombre = self.entry_nombre.get().strip()
        if nombre:
            mensaje = f"Hola {nombre}"
            messagebox.showinfo("Saludo", mensaje)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre.")

# Ejecución del programa
if __name__ == "__main__":
    root = tk.Tk()
    app = SaludoApp(root)
    root.mainloop()
