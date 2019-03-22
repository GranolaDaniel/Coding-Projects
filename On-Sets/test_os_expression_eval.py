import unittest
from os_expression_eval import Interpreter, Lexer, Parser

Interpreter.Universe = [frozenset(), frozenset({'B', 'G'}), frozenset({'R'}), frozenset({'Y', 'B', 'R', 'G'}), frozenset({'B', 'R'}), frozenset({'G'}), frozenset({'Y', 'R', 'G'}), frozenset({'Y'}), frozenset({'Y', 'B'}), frozenset({'Y', 'B', 'R'}), frozenset({'R', 'G'})]

class TestTokenizer(unittest.TestCase):
    def get_parse(self, solution):
        lexer = Lexer(solution)

        return Parser(lexer)

    def test_BUR(self):
        self.assertFalse(repr(self.get_parse('B - R - Y')))

class TestExpr(unittest.TestCase):

    def get_solution(self, solution):
        lexer = Lexer(solution)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)

        return interpreter.interpret()

    def test_union(self):
        result = self.get_solution('B U R')
        self.assertEqual(len(result), 8)

    def test_intersect(self):
        result = self.get_solution('Y n R')
        self.assertEqual(len(result), 3)

    def test_difference(self):
        result = self.get_solution('B - R')
        self.assertEqual(len(result), 2)

    def test_compliment(self):
        result = self.get_solution('Y\'')
        self.assertEqual(len(result), 6)

    def test_compound_union(self):
        result = self.get_solution('B U R U Y')
        self.assertEqual(len(result), 9)

        with self.subTest(result=self.get_solution('(B U R) U Y')):
            self.assertEqual(len(result), 9)

    def test_compound_intersect(self):
        result = self.get_solution('B n R n Y')
        self.assertEqual(len(result), 2)

        with self.subTest(result=self.get_solution('(B n R) n Y')):
            self.assertEqual(len(result), 2)

    def test_compound_difference(self):
        result = self.get_solution('B - R - Y')
        self.assertEqual(len(result), 1)

        with self.subTest(result=self.get_solution('(B - R) - Y')):
            self.assertEqual(len(result), 1)

    def test_compound_compliment(self):
        result = self.get_solution('(B U R)\'')
        self.assertEqual(len(result), 3)



if __name__ == '__main__':
    unittest.main()