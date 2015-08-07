import re

token_pat = re.compile("\s*(?:(\d+)|(.))")

class end_token:
    lbp = 0

class literal_token:
    def __init__(self,value):
        self.value = int(value)

    def nud(self):
        return self.value

class operator_add_token:
    lbp = 10
    def nud(self):
        return expression(100)

    def led(self,left):
        right = expression(10)
        return left + right

class operator_substract_token:
    lbp = 10
    def nud(self):
        return -expression(100)
    def led(self,left):
        right = expression(10)
        return left - right

class operator_division_token:
    lbp = 20
    def led(self,left):
        return left / expression(20)

class operator_multiply_token:
    lbp = 20
    def led(self,left):
        return left * expression(20)

def tokenize(program):
    for number, operator in token_pat.findall(program):
        if number:
            yield literal_token(number)
        elif operator == '+':
            yield operator_add_token()
        elif operator == "/":
            yield operator_division_token()
        elif operator == "-":
            yield operator_substract_token()
        elif operator == "*":
            yield operator_multiply_token()
        else:
            raise SyntaxError('Unknown Operator')
    yield end_token()

def expression(rbp=0):
    global token
    t = token
    token = next()
    left = t.nud()
    while rbp < token.lbp:
        t = token
        token = next()
        left = t.led(left)
    return left

def parse(program):
    global token, next
    next = tokenize(program).next
    token = next()
    return expression()

