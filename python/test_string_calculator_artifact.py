import unittest
from main import main as calculator, add


class Test_String_Calculator(unittest.TestCase):
    def test_add(self):


        self.assertEqual(calculator(""), 0)
        self.assertEqual(calculator("1"), 1)
        self.assertEqual(calculator("1,2"), 3)
        self.assertEqual(calculator("0,1"), 1)
        self.assertEqual(calculator("1,2,3"), 6)
        self.assertEqual(calculator("1,2,3,4,5"), 15)
        self.assertEqual(calculator("1,2,3,4,5,6"), 21)
        self.assertEqual(calculator("1,2\n3,4\n5,6\n7"), 28)
        self.assertEqual(calculator("1\n2,3\n4,5,6\n7,8"), 36)
        self.assertEqual(calculator("2,a3"), 5)
        self.assertEqual(calculator("//;\n1;2"), 3)
        self.assertEqual(calculator("/1,2/;\n3ESTO?ES.UN.STEST'5,2,2"), 15)
        self.assertEqual(calculator("1520,2,3"), 1525)
        self.assertEqual(calculator("//[***]\n1***8***3"), 12)
        self.assertEqual(calculator("//[*][%]\n1*2%5"), 8)
        self.assertEqual(calculator("//[***][%%]\n1***2%%3"), 6)



class TestNegativeNumbers(unittest.TestCase):
    def test_negative_numbers_exception(self):


        input_numbers = "-1,5,10,-5,-3"


        with self.assertRaises(Exception) as context:
            add(input_numbers)
       
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -5, -3")




if __name__ == '__main__':
    unittest.main()
