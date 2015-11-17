import unittest
from parser import evaluate as p

class TestParser(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(p("3+5"),8)
    def test_substraction(self):
        self.assertEqual(p("3-5"),-2)
    def test_division(self):
        self.assertEqual(p("10/2"),5)
    def test_multiplication(self):
        self.assertEqual(p("3*4"),12)
    def test_division_with_space(self):
        self.assertEqual(p("10 /2"),5)
    def test_multiplication_with_space(self):
        self.assertEqual(p("10 * 2"),20)
    def test_addition_substraction(self):
        self.assertEqual(p("3+5-8"),0)
        self.assertEqual(p("3-8+5"),0)
    def test_addition_multiplication(self):
        self.assertEqual(p("5*2-3"),7)
        self.assertEqual(p("-3+5*2"),7)
    def test_addition_with_parenthesis(self):
        self.assertEqual(p("(5 + 4)"),9)
        self.assertEqual(p("(5 + 4)*4"),36)

if __name__ == '__main__':
    unittest.main()



