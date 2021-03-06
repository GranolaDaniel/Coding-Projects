from random import choice, randint

###############################################################################
#                                                                             #
#  SETUP                                                                      #
#                                                                             #
###############################################################################

#Materials and conditions
#Colors
B, R, G, Y = ('B', 'R', 'G', 'Y')
ColorSet = [B, R, G, Y]

def cubeRoll(Cube):
            Resources.append(choice(Cube))
#Cubes
U, n, V, A, C = ('U', 'n', 'V', 'A', 'C')
DigitCube = [1, 2, 3, 4, 5]
ColorCube = [B, R, G, Y]

#I'll leave some op cubes as strings for now
OperationCube = [U, n, '-', '\'']
RestrictionCube = [V, A, '=', C]

#Cards: Have unique combination of zero to four colors
Cards = [frozenset([B]), frozenset([R]), frozenset([G]), frozenset([Y]), frozenset([B, R]), frozenset([B, G]), frozenset([B, Y]), frozenset([R, G]), frozenset([R, Y]), frozenset([G, Y]),
frozenset([B, R, G, Y]), frozenset([]), frozenset([B, R, G]), frozenset([B, R, Y]), frozenset([R, G, Y]), frozenset([B, G, Y])]

#Mat
Required = []
Permitted = []
Forbidden = []

Goal = []

Resources = []
#Variations


class Universe(object):
    def __init__(self):
        self.Universe = self.create()
        self.size = len(self.Universe)

    def create(self):
        universeSize = int(input('Choose the size of the universe> '))
        Universe = []
        while len(Universe) != universeSize:
            Universe.append(Cards.pop(Cards.index(choice(Cards))))
        return Universe

def universeCreate():
    universeSize = int(input('Choose the size of the universe> '))
    Universe = []
    while len(Universe) != universeSize:
        Universe.append(Cards.pop(Cards.index(choice(Cards))))
    return Universe

###############################################################################
#                                                                             #
#  LEXER                                                                      #
#                                                                             #
###############################################################################

#Token types
COLOR, UNION, INTERSECT, MINUS, COMPLIMENT, UNIVERSE_OP, EMPTY_S, EQUALS, SUBSET, L_PAREN, R_PAREN, EOF = ('COLOR', 'UNION', 'INTERSECT', 'MINUS', 'COMPLIMENT', 'UNIVERSE_OP', 'EMPTY_S',
    'EQUALS', 'SUBSET', 'L_PAREN', 'R_PAREN', 'EOF')

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = repr(self.value)
        )
    def __repr__(self):
        return self.__str__()

class Lexer(object):
    def __init__(self, text):
        #Text is the actual solution input as a string
        self.text = text
        #A marker for iterating through each value of the solution
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        #Advances position pointer and sets current character variable
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None #End of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char in ['B', 'R', 'G', 'Y']:
                temp_char = self.current_char
                self.advance()
                return Token(COLOR, temp_char)

            if self.current_char == 'U':
                self.advance()
                return Token(UNION, 'U')

            if self.current_char == 'n':
                self.advance()
                return Token(INTERSECT, 'n')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '\'':
                self.advance()
                return Token(COMPLIMENT, '\'')

            if self.current_char == 'V':
                self.advance()
                return Token(UNIVERSE_OP, 'V')

            if self.current_char == 'A':
                self.advance()
                return Token(EMPTY_S, 'A')

            if self.current_char == '=':
                self.advance()
                return Token(EQUALS, '=')

            if self.current_char == 'C':
                self.advance()
                return Token(SUBSET, 'C')

            if self.current_char == '(':
                self.advance()
                return Token(L_PAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(R_PAREN, ')')

            self.error()

        return Token(EOF, None)

###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################
class AST(object):
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right
        self.solution = []

    def __repr__(self):
        return 'BinOP --> (left: {}, op: {}, right: {})'.format(self.left, self.op, self.right)

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value
        self.solution = []

    def __repr__(self):
        return 'Num: {}'.format(self.value)
class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        #Sets the current token to the first token taken from the solution
        self.current_token = self.lexer.get_next_token()

    def __repr__(self):
        return 'Node --> {}'.format(repr(self.parse()))

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor: COLOR | EMPTY_S | UNIVERSE_OP | L_PAREN expr R_PAREN"""
        token = self.current_token

        if token.type in (COLOR, EMPTY_S, UNIVERSE_OP):
            self.eat(token.type)
            return Num(token)
        elif token.type == L_PAREN:
            self.eat(L_PAREN)
            node = self.expr()
            self.eat(R_PAREN)
            return node

    def term(self):
        """term: factor COMPLIMENT"""
        node = self.factor()

        while self.current_token.type is COMPLIMENT:
            token = self.current_token
            self.eat(COMPLIMENT)

            node = BinOp(left = node, op = token, right = self.expr())

        return node

    def expr(self):
        """expr: term (UNION | INTERSECT | MINUS | SUBSET | EQUALS) term"""
        """expr: expr (UNION | INTERSECT | MINUS | SUBSET | EQUALS) expr"""
        node = self.term()

        while self.current_token.type in (UNION, INTERSECT, MINUS, SUBSET, EQUALS):
            token = self.current_token

            if token.type == UNION:
                self.eat(UNION)
            elif token.type == INTERSECT:
                self.eat(INTERSECT)
            elif token.type == MINUS:
                self.eat(MINUS)
            elif token.type == SUBSET:
                self.eat(SUBSET)
            elif token.type == EQUALS:
                self.eat(EQUALS)

            else:
                self.error()

            node = BinOp(left = node, op = token, right = self.expr())

        return node

    def parse(self):
        return self.expr()

###############################################################################
#                                                                             #
#  INTERPRETER                                                                #
#                                                                             #
###############################################################################

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def populate(self, node):
       if type(node) == BinOp:
            if type(node.left) == BinOp:
                self.populate(node.left)
                self.visit_BinOp(node.left)

            if len(node.left.solution) == 0 and (node.left.value == 'V' or node.left.value == 'A'):
                if node.left.value == 'V':
                    node.left.solution = frozenset(self.Universe)
                elif node.left.value == 'A':
                    node.left.solution = frozenset({frozenset({})})
            elif len(node.left.solution) == 0 and type(node.left) != BinOp:
                for i in self.Universe:
                    if node.left.value in i:
                        node.left.solution.append(i)
                node.left.solution = frozenset(node.left.solution)

            if type(node.right) == BinOp:
                self.populate(node.right)
                self.visit_BinOp(node.right)
            try:
                if len(node.right.solution) == 0 and (node.right.value == 'V' or node.right.value == 'A'):
                    if node.right.value == 'V':
                        node.right.solution = frozenset(self.Universe)
                    elif node.right.value == 'A':
                        node.right.solution = frozenset({frozenset({})})
                elif len(node.right.solution) == 0 and type(node.right) != BinOp:
                    for i in self.Universe:
                        if node.right.value in i:
                            node.right.solution.append(i)
                    node.right.solution = frozenset(node.right.solution)
            except AttributeError:
                pass
       elif type(node) == Num:
           if node.value == 'V':
               node.solution = self.Universe
           elif node.value == 'A':
               node.solution = frozenset({})
           else:
             for i in self.Universe:
               if node.value in i:
                   node.solution.append(i)
           node.solution = frozenset(node.solution)


    def visit_BinOp(self, node):
        if type(node.left) == BinOp:
            self.visit_BinOp(node.left)
        if type(node.right) == BinOp:
            self.visit_BinOp(node.right)

        if node.op.type == UNION:
            node.solution = node.left.solution.union(node.right.solution)
        elif node.op.type == INTERSECT:
            node.solution = node.left.solution.intersection(node.right.solution)
        elif node.op.type == COMPLIMENT:
            node.solution = node.left.solution.symmetric_difference(frozenset(self.Universe))
        elif node.op.type == MINUS:
            node.solution = node.left.solution.difference(node.right.solution)

        return node.solution


    def visit_Num(self, node):
        if node.token.type == EMPTY_S:
            if node.solution in self.Universe:
                return node.solution
        if node.token.type == UNIVERSE_OP:
            return node.solution
        if node.token.type == COLOR:
            return node.solution


    def interpret(self):
        tree = self.parser.parse()
        self.populate(tree)
        return self.visit(tree)

def main():
    while True:
        try:
            Interpreter.Universe = universeCreate()
            print(Interpreter.Universe)
            ent_solution = input('Enter solution> ')
        except EOFError:
            print('Try using python3 <3')
            break
        if not ent_solution:
            continue

        lexer = Lexer(ent_solution)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)

if __name__ == '__main__':
    main()
