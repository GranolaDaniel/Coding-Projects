from random import choice, randint
import math
import os_expression_eval

#Materials and conditions
#Colors
B = Color('B')
R = Color('R')
G = Color('G')
Y = Color('Y')
ColorSet = {B, R, G, Y}

#Cubes
U = '\u22C3'
n = '\u22C2'
V = '\u22C1' #Or 22BB
A = '\u22C0'
C = '\u2286'

DigitCube = [1, 2, 3, 4, 5]
ColorCube = [B, R, G, Y]
#I'll leave some op cubes as strings for now
OperationCube = [U, n, '-', '\'']
RestrictionCube = [V, A, '=', C]
#Cards: Have unique combination of zero to four colors
Cards = [{B}, {R}, {G}, {Y}, {B, R}, {B, G}, {B, Y}, {R, G}, {R, Y}, {G, Y}, {B, R, G, Y}, {}, {B, R, G}, {B, R, Y}, {R, G, Y}, {B, G, Y}]
#Mat
Required = []
Permitted = []
Forbidden = []

Goal = []

Resources = []
Universe = set()
#Variations
#Generic cube roll function
def cubeRoll(Cube):
	Resources.append(choice(Cube))
def universeCreate():
	universeSize = int(input('Choose the size of the universe'))
	while len(Universe) != universeSize:
		Universe.pop(choice(Cards))
#Op functions
def Union(x,y):
	return x | y
def Intersect(x,y):
	inter = {x, y}
	return inter
def Difference(x,y):

def Compliment(x):
	comp = set()
	for i in ColorSet:
		if i != x:
			comp.add(i)
	return comp
def Equals(x,y):

def Subset(x,y):


#Dictionary with op functions
ops_dict = {'U': Union,
			'n': Intersect,
			'-': Difference,
			'\'': Compliment, 
			'=': Equals,
			'C': Subset
		}
#New game setup




