import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from Saludo_en_GUI import SaludoApp  # Asegúrate de que esté en el mismo directorio o usa ruta relativa

class TestSaludoApp(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de la app sin mostrar ventana
        self.root = tk.Tk()
        self.root.withdraw()  # Oculta la ventana principal
        self.app = SaludoApp(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.messagebox.showinfo')
    def test_saludo_con_nombre(self, mock_showinfo):
        self.app.entry_nombre.insert(0, "Carlos")
        self.app.saludar()
        mock_showinfo.assert_called_once_with("Saludo", "Hola Carlos")

    @patch('tkinter.messagebox.showwarning')
    def test_saludo_sin_nombre(self, mock_showwarning):
        self.app.entry_nombre.delete(0, tk.END)
        self.app.saludar()
        mock_showwarning.assert_called_once_with("Advertencia", "Por favor, ingrese un nombre.")

if __name__ == '__main__':
    unittest.main()
