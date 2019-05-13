from random import sample
from lark import Lark, Transformer

B, R, G, Y = ('B', 'R', 'G', 'Y')

class Universe(object):

    #Cards: Have unique combination of zero to four colors
    Cards = [frozenset([B]), frozenset([R]), frozenset([G]), frozenset([Y]), frozenset([B, R]), frozenset([B, G]), frozenset([B, Y]), frozenset([R, G]), frozenset([R, Y]), frozenset([G, Y]),
    frozenset([B, R, G, Y]), frozenset([]), frozenset([B, R, G]), frozenset([B, R, Y]), frozenset([R, G, Y]), frozenset([B, G, Y])]

    def universeCreate(self, size=10):
        universeSize = int(size)
        Universe = sample(self.Cards, k=universeSize)
        
        return Universe

grammar = '''solution: (restriction "/")? expr
        
        ?expr: "(" expr ")"                                 
            | unary                                         
            | COLOR                                         -> color_expr
            | SET_CUBE                                      -> set_expr
            | expr OPERATOR expr                            -> op_expr
        
        unary: expr COMPLIMENT                              -> compliment_expr
        
        ?restriction: "(" restriction ")"                   
            | expr                                      
            | restriction SET_OP restriction                -> restriction_expr
        
        COLOR: "B" | "R" | "G" | "Y"
        SET_CUBE: "V" | "A"
        OPERATOR: "U" | "n" | "-"
        COMPLIMENT: "\'"
        SET_OP: "C" | "="
        
        %ignore " "
'''

parser = Lark(grammar, start='solution', ambiguity="explicit")

class CalcTransformer(Transformer):
    def __init__(self, universe):
        self.universe = universe

    def color_expr(self, args):
        solution_dict = {args[0].value: set()}

        for i in self.universe:
            if args[0].value in i:
                solution_dict[args[0].value].add(i)
        
        return solution_dict[args[0]]
    
    def set_expr(self, args):
        solution_dict = {args[0].value: set()}

        if args[0].value == 'V':
            for i in self.universe:
                solution_dict[args[0].value].add(i)
        elif args[0].value == 'A' and frozenset([]) in self.universe:
            solution_dict[args[0].value].add(frozenset([]))
        return solution_dict[args[0]]

    def op_expr(self, args):
        solution_dict = {}
        
        operator = args[1].value
        left_arg = args[0]
        right_arg = args[2]

        if isinstance(left_arg, tuple):
            left_arg = left_arg[1]
        if isinstance(right_arg, tuple):
            right_arg = right_arg[1]
    
        if operator == 'U':
            solution_dict[operator] = left_arg.union(right_arg)
            return (operator, solution_dict[operator])
        elif operator == 'n':
            solution_dict[operator] = left_arg.intersection(right_arg)
            return (operator, solution_dict[operator])
        elif operator == '-':
            solution_dict[operator] = left_arg.difference(right_arg)
            return (operator, solution_dict[operator])
        else:
            return 'error'
    
    def compliment_expr(self, args):
        solution_dict = {'comp': set()}
        
        arg = args[0]
        if isinstance(arg, tuple):
            arg = arg[1]
        for i in self.universe:
                solution_dict['comp'].add(i)
        solution_dict['comp'].symmetric_difference_update(arg)

        return solution_dict['comp']
    
    def restriction_expr(self, args):
        # operator = args[1].value

        # if operator in ['U', 'n', '-']:
        #     return self.op_expr(args)
        # elif operator == '\'':
        #     return self.compliment_expr(args)
        
        # elif operator == 'C':
        #     #Return subset
        #     pass
        # elif operator == '=':
        #     #Return equals
        #     pass
        pass

def Temp_Parse(text):
    parsed = parser.parse(text)
    return parsed

def subtrees(parsed):
    return parsed.iter_subtrees()