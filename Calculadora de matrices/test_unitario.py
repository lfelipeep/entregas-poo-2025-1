import unittest
from Calculadora import Matriz

class TestMatriz(unittest.TestCase):
    def test_suma(self):
        m1 = Matriz([[1, 2], [3, 4]])
        m2 = Matriz([[5, 6], [7, 8]])
        resultado = m1 + m2
        esperado = [[6, 8], [10, 12]]
        self.assertEqual(resultado.elementos, esperado)

    def test_resta(self):
        m1 = Matriz([[5, 5], [5, 5]])
        m2 = Matriz([[2, 3], [1, 4]])
        resultado = m1 - m2
        esperado = [[3, 2], [4, 1]]
        self.assertEqual(resultado.elementos, esperado)

    def test_multiplicacion(self):
        m1 = Matriz([[1, 2], [3, 4]])
        m2 = Matriz([[2, 0], [1, 2]])
        resultado = m1 * m2
        esperado = [[4, 4], [10, 8]]
        self.assertEqual(resultado.elementos, esperado)

if __name__ == "__main__":
    unittest.main()
