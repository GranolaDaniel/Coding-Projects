from constraint import *
from random import choice, randint

###############################################################################
#                                                                             #
#  SETUP                                                                      #
#                                                                             #
###############################################################################

#Materials and conditions
#Colors
B = 'B'
R = 'R'
G = 'G'
Y = 'Y'
ColorSet = [B, R, G, Y]

#Cubes
U = 'U' #\u22C3
n = 'n' #\u22C2
V = 'V' #\u22C1 or 22BB
A = 'A' #\u22C0
C = 'C' #\u2286

DigitCube = [1, 2, 3, 4, 5]
ColorCube = [B, R, G, Y]
#I'll leave some op cubes as strings for now
OperationCube = [U, n, '-', '\'']
RestrictionCube = [V, A, '=', C]
#Cards: Have unique combination of zero to four colors
Cards = [[B], [R], [G], [Y], [B, R], [B, G], [B, Y], [R, G], [R, Y], [G, Y], 
[B, R, G, Y], [], [B, R, G], [B, R, Y], [R, G, Y], [B, G, Y]]
#Mat
Required = []
Permitted = []
Forbidden = []

Goal = []

Resources = []
#Variations
#Generic cube roll function
def cubeRoll(Cube):
	Resources.append(choice(Cube))

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
		#Shows class as string, e.g. Token(Color, B)
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
		#This is the method responsible for breaking the solution into tokens (tokenizer)
		while self.current_char is not None:

			if self.current_char.isspace():
				self.skip_whitespace()
				continue

			if self.current_char in ['B', 'R', 'G', 'Y']:
				return Token(COLOR, self.current_char)
				self.advance()

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

class Num(AST):
	def __init__(self, token):
		self.token = token
		self.value = token.value

class Parser(object):
	def __init__(self, lexer):
		self.lexer = lexer
		#Sets the current token to the first token taken from the solution
		self.current_token = self.lexer.get_next_token()

	def error(self):
		raise Exception('Invalid syntax')

	def eat(self, token_type):
		if self.current_token.type == token_type:
			self.current_token = self.lexer.get_next_token()
		else:
			self.error()

	def factor(self):
		#factor: COLOR | EMPTY_S | UNIVERSE_OP | L_PAREN expr R_PAREN -- Leaf nodes
		token = self.current_token
		if token.type == COLOR:
			self.eat(COLOR)
			return Num(token)
		
		if token.type == EMPTY_S:
			self.eat(EMPTY_S)
			return Num(token)

		if token.type == UNIVERSE_OP:
			self.eat(UNIVERSE_OP)
			return Num(token)

		elif token.type == L_PAREN:
			self.eat(L_PAREN)
			node = self.expr()
			self.eat(R_PAREN)
			return node

	def term(self):
		#term: (factor) COMPLIMENT e.g. G', (B U R)'
		node = self.factor()

		while self.current_token.type is COMPLIMENT:
			token = self.current_token
			self.eat(COMPLIMENT)

			node = BinOp(left = node, op = token, right = self.expr())

		return node

	def expr(self):
		#Makes sure that current token type matches expected token type
		node = self.term()

		while self.current_token.type in (UNION, INTERSECT, MINUS):
			token = self.current_token
			if token.type == UNION:
				self.eat(UNION)
			elif token.type == INTERSECT:
				self.eat(INTERSECT)
			elif token.type == MINUS:
				self.eat(MINUS)

			node = BinOp(left = node, op = token, right = self.term())

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
	#Edit so Solution list == Universe and is accessible to the visit methods
	solution_list = universeCreate()

	def visit_BinOp(self, node):
		if node.op.type == UNION:
			for i in Interpreter.solution_list:
				if self.visit(node.left) not in Interpreter.solution_list[i] and self.visit(node.right) not in Interpreter.solution_list[i]:
					Interpreter.solution_list.remove(Interpreter.solution_list[i])
					return Interpreter.solution_list

		if node.op.type == INTERSECT:
			for i in Interpreter.solution_list:
				if self.visit(node.left) not in Interpreter.solution_list[i] or self.visit(node.right) not in Interpreter.solution_list[i]:
					Interpreter.solution_list.remove(Interpreter.solution_list[i])
					return Interpreter.solution_list

		#if node.op.type == COMPLIMENT: 
			#TODO COMPLIMENT OPERATION

		if node.op.type == MINUS:
			for i in Interpreter.solution_list:
				if self.visit(node.left) not in Interpreter.solution_list[i] or (self.visit(node.left) in Interpreter.solution_list[i] and self.visit(node.right) in Interpreter.solution_list[i]):
					Interpreter.solution_list.remove(Interpreter.solution_list[i])
					return Interpreter.solution_list


	def visit_Num(self, node):
		return node.value

	def interpret(self):
		tree = self.parser.parse()
		return self.visit(tree)

def main():
	while True:
		try:
			ent_solution = input('Enter solution> ')
		except EOFError:
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

"""
class Solution:

	def __init__(self, expression):
		self.expression = expression
		self.items = []
		self.working_list = []

	def separate(self):
		for i, char in enumerate(self.expression):
			if char != ' ':
				self.items.append((i, char))
		#Define ops
		for i, char in self.items:
			if char == 'U':
				char = UnionOp(i)
				self.working_list.insert(i, char)
			elif char == 'n':
				char = IntersectOp(i)
				self.working_list.insert(i, char)
			elif char == '-':
				char = DiffOp(i)
				self.working_list.insert(i, char)
			elif char == '\'':
				char = ComplimentOp(i)
				self.working_list.insert(i, char)
		#Define colors
			elif char == 'B' or char == 'R' or char == 'G' or char == 'Y':
				char = Color(char)
				self.working_list.insert(i, char)
		#Define restrictions
			elif char == 'C' or char == '\u2286':
				char = SubsetOp(i)
				self.working_list.insert(i, char)
			elif char == '=':
				char = EqualsOp(i)
				self.working_list.insert(i, char)

#Operators
class Operator:

	def __init__(self, sym):
		self.sym = sym

class UnionOp(Operator):
	
	def __init__(self, ind):
		self.ind = ind
		Operator.__init__(self, 'U')
		self.working_list = []

	def evaluate(self):
		left_Char = Solution.working_list[self.ind - 1]
		right_Char = Solution.working_list[self.ind + 1]
	#Evaluate as a new set that's a union of l/r color
		if isinstance(left_Char, Color) == Color and isinstance(right_Char, Color) == Color:
			self.working_list.append(left_Char | right_Char)

class IntersectOp(Operator):

	def __init__(self, ind):
		self.ind = ind
		Operator.__init__(self, 'n')
class DiffOp(Operator):

	def __init__(self, ind):
		self.ind = ind
		Operator.__init__(self, '-')
class ComplimentOp(Operator):

	def __init__(self, ind):
		self.ind = ind
		Operator.__init__(self, '\'')
		self.working_list = []
	
	def evaluate(self):
		
		comp_char = Solution.working_list[self.ind - 1]
		poss_color = ['B', 'R', 'G', 'Y']
	#Makes set of all compliments of color var 
		if type(comp_char) == Color:
			for i in poss_color:
				if set(i) != comp_char.color_set:
					self.working_list.append(set(i))
#Restrictions
class SubsetOp(Operator):

	def __init__(self, ind):
		self.ind = ind
		Operator.__init__(self, '\u2286')
class EqualsOp(Operator):

	def __init__(self, ind):
		self.ind = ind
		Operator.__init__(self, '=')
#Colors
class Color:

	def __init__(self, color):
		self.color = color
		self.color_set = set(color)
"""