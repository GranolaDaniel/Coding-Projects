from os_expression_eval import Token, UNION, INTERSECT, MINUS, COMPLIMENT, COLOR, Num, BinOp, Interpreter

BlueToken = Token(COLOR, 'B')
MinusToken = Token(MINUS, '-')
RedToken = Token(COLOR, 'R')
CompToken = Token(COMPLIMENT, '\'')
UnionToken = Token(UNION, 'U')
GreenToken = Token(COLOR, 'G')
#B U (R - G)
RMinG = BinOp(
	left = Num(RedToken),
	op = MinusToken,
	right = Num(GreenToken)
	)
UB = BinOp(
	left = RMinG,
	op = UnionToken,
	right = Num(BlueToken)
	)

inter = Interpreter(None)
print(inter.visit(UB))
