from ejercicio import total, addit, mult, divide,length,reverse,remove_letter,max,even_numbers,odd_numbers,is_even
import unittest

class TestEjercicio(unittest.TestCase):
    def test_total(self):
        lst=[3,2,1,5]
        res = total(lst)
        self.assertEqual(11, res)

    def test_addit(self):
        res = addit(4)
        self.assertEqual(9, res)

    def test_mult(self):
        res = mult(3)
        self.assertEqual(24, res)

    def test_divide (self):
        res = divide(10,5)
        self.assertEqual(2, res)
        
        self.assertRaises(ZeroDivisionError,divide,10,0)    

# Calcula el tamaño de una lista o string y devuelve un valor segun el tamaño

    def test_length(self):
        res = length("Hola")
        self.assertEqual("Less than 5", res)
        res = length("Hola Mundo")
        self.assertEqual("Longer than 5", res)
        res = length("Holas")
        self.assertEqual("Longer than 5", res)

        res = length([1, 2, 3])
        self.assertEqual("Less than 5", res)
        res = length([1, 2, 3, 4, 5, 6])
        self.assertEqual("Longer than 5", res)
        res = length([1, 2, 3, 4, 5])
        self.assertEqual("Longer than 5", res)
       

#Recibe un string y lo devulve al reves -> Ejemplo: casa -> asac

    def test_reverse(self):
        res = reverse("Reconocer")
        self.assertEqual("reconoceR", res)
        res = reverse("Python")
        self.assertEqual("nohtyP", res)

#Recibe por parametro un string y una letra y se reemplaza la letra que se requera

    def test_remove_letter(self):
        res = remove_letter("a", "Hola")
        self.assertEqual("Hol", res)
        res = remove_letter("o", "oso")
        self.assertEqual("s", res)

#Recibe una arreglo de numeros y devuelve el numero mayor

    def test_max(self):
        res = max([1, 8, 3, 6, 12, 5])
        self.assertEqual(12, res)
        res = max([1, 5, 5, 4.99, 5.01])
        self.assertEqual(5.01, res)
        res = max([-1, 5, -5, -4.99, -5.01])
        self.assertEqual(5, res)

#recibe una lista de numeros y devuelve solo los elementos pares

    def test_even_numbers(self):
        res = even_numbers([1, 2, 3, 4, 5, 6])
        self.assertEqual([2, 4, 6], res)
        res = even_numbers([0, 3, 5, 7, 9])
        self.assertEqual([0], res)

#recibe una lista de numeros y devuelve solo los elementos impares

    def test_odd_numbers(self):
        res = odd_numbers([1, 2, 3, 4, 5, 6])
        self.assertEqual([1, 3, 5], res)
        res = odd_numbers([0, 3, 5, 7, 9])
        self.assertEqual([3, 5, 7, 9], res)

#Recibe un numero, y devuelve un booleano, donde indica si es par

    def test_is_even(self):
        res = is_even(23)
        self.assertEqual(False, res)
        res = is_even(0)
        self.assertEqual(True, res)












    
if __name__ == '__main__':
    unittest.main()
