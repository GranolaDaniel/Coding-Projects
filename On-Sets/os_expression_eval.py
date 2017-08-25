from constraint import *

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