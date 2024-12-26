import unittest
from string_calculator_artifact import add

class Test_String_Calculator(unittest.TestCase):
    def test_add(self):

        self.assertEqual(add(""), 0)
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("1,2"), 3)
        self.assertEqual(add("0,1"), 1)
        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("1,2,3,4,5"), 15)
        self.assertEqual(add("1,2,3,4,5,6"), 21)
        self.assertEqual(add("1,2\n3,4\n5,6\n7"), 28)
        self.assertEqual(add("1\n2,3\n4,5,6\n7,8"), 36)
        self.assertEqual(add("2,a3"), 5)
        self.assertEqual(add("//;\n1;2"), 3)
        self.assertEqual(add("/1,2/;\n3ESTO?ES.UN-TEST'5,2,2"), 15)


if __name__ == '__main__':
    unittest.main()