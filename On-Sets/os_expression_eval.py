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
#Testing
	Universe = universeCreate()
	print(Universe)
	solution_list = []
#End testing
	def visit_BinOp(self, node):
		if node.op.type == UNION:
			for i in Interpreter.Universe:
				if self.visit(node.left) in i or self.visit(node.right) in i:
					Interpreter.solution_list.append(i)
			
		if node.op.type == INTERSECT:
			for i in Interpreter.Universe:
				if self.visit(node.left) in i and self.visit(node.right) in i:
					Interpreter.solution_list.append(i)
			
		if node.op.type == COMPLIMENT: 
			for i in Interpreter.Universe:
				if self.visit(node.left) not in i:
					Interpreter.solution_list.append(i)
			
		if node.op.type == MINUS:
			if len(Interpreter.solution_list) > 1:
				for i in Interpreter.solution_list:
					if self.visit(node.right) in i:
						Interpreter.solution_list.remove(i)

			for i in Interpreter.Universe:
				if self.visit(node.left) in i and self.visit(node.right) not in i:
					Interpreter.solution_list.append(i)
		
		return Interpreter.solution_list


	def visit_Num(self, node):
	#Edit for Empty Set and Universe Op
		if node.token.type == EMPTY_S:
			for i in Interpreter.Universe:
				if i == []:
					Interpreter.solution_list.append(i)
		
		if node.token.type == UNIVERSE_OP:
			for i in Interpreter.Universe:
				Interpreter.solution_list.append(i)

		if node.token.type == COLOR:
			for i in Interpreter.Universe:
				if node.value in i:
					Interpreter.solution_list.append(i)
			
		return Interpreter.solution_list

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