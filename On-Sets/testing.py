from os_expression_eval import *
from constraint import *

problem = Problem()

problem.addVariable("a", [1,2,3])
problem.addVariable("b", [4,5,6])

problem.addConstraint(lambda a, b: a*2 == b, ("a", "b"))

print(problem.getSolutions())