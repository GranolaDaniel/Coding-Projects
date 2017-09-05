from random import choice, randint
import math
import os_expression_eval


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





