import unittest
from parser import evaluate as p

class TestParser(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(p("3+5"),8)
        self.assertEqual(p("3 + 5"),8)
    def test_substraction(self):
        self.assertEqual(p("3-5"),-2)
        self.assertEqual(p("3 - 5"),-2)
    def test_division(self):
        self.assertEqual(p("10/2"),5)
        self.assertEqual(p("10 / 2"),5)
    def test_multiplication(self):
        self.assertEqual(p("3*4"),12)
        self.assertEqual(p("-1*35"),-35)
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
    def test_division_with_parenthesis(self):
        self.assertEqual(p("(6/2)/3"),1)
        self.assertEqual(p("(6 /2)/ 3"),1)
        self.assertEqual(p("( 6/2 )/3"),1)
    def test_multiplication_addition(self):
        self.assertEqual(p("5 * (3 + 4)"),35)
        self.assertEqual(p("5 + (3 * 4)"),17)
    def test_only_parenthesis(self):
        self.assertEqual(p("(35)"),35)
        self.assertEqual(p("-(35)"),-35)
        self.assertEqual(p("3(35)"),105)
        self.assertEqual(p("(35)3"),105)
    def test_paranthesis_substraction(self):
        self.assertEqual(p("(30)-3"),27)
        self.assertEqual(p("-3(30)"),-90)
        self.assertEqual(p("-3 (30)"),-90)
        self.assertEqual(p("(33-3)(30)"),900)
    def test_pi(self):
        self.assertEqual(p("pi * 3"),9.42477796076938)
        self.assertEqual(p("(pi)* 3"),9.42477796076938)
        self.assertEqual(p("(pi)3"),9.42477796076938)
    def test_exponent(self):
        self.assertEqual(p("3^2"),9)
        self.assertEqual(p("5 ^ 3"),125)

if __name__ == '__main__':
    unittest.main()
