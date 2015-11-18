import math

class Parser:
    
    def __init__(self,string,vars={}):
        self.string = string
        self.index = 0
        self.vars = {
                "pi" : math.pi,
                "e" : math.e 
                  }
        for var in vars.keys():
            if self.vars.get(var) != None:
                # If the key is already present then raise the exception
                raise Exception("Cannot redefine the value of " + var)
            self.vars[var] = vars[var]


    def get_value(self):
        value = self.parse_expression()
        self.skip_whitespace()
        if self.has_next():
            raise Exception("Unexpected character found '" + self.peek() +"' at index " + str(self.index))
        return value


    def peek(self):
        return self.string[self.index : self.index + 1]


    def has_next(self):
        return self.index < len(self.string)


    def skip_whitespace(self):
        while self.has_next():
            if self.peek() in ' \t\n\r':
                self.index += 1
            else:
                return


    def parse_expression(self):
        value = self.parse_addition()
        return value


    def parse_addition(self):
        values = [self.parse_multiplication()]
        while True:
            self.skip_whitespace()
            char = self.peek()
            if char == '+':
                self.index += 1
                values.append(self.parse_multiplication())
            elif char == '-':
                self.index += 1
                values.append(-1 * self.parse_multiplication())
            else:
                break

        return sum(values)

    def parse_exponent(self):
        values = self.parse_parenthesis()
        exp = 1
        while True:
            self.skip_whitespace()
            char = self.peek()
            if char == '^':
                self.index += 1
                exp = self.parse_parenthesis()
            else:
                break
        return values**exp



    def parse_multiplication(self):
        values = [self.parse_exponent()]
        while True:
            self.skip_whitespace()
            char = self.peek()
            if char  == '*':
                self.index += 1
                values.append(self.parse_exponent())
            elif char == '/':
                div_index = self.index
                self.index += 1
                denominator = self.parse_exponent()
                if denominator == 0:
                    raise Exception("Division by zero kills babies")
                values.append(1.0/denominator)
            elif char == '(':
                # handle the case when no multiplication is defined on brackets are given eg. 4(34)
                values.append(self.parse_exponent())
            elif char and char in '0123456789':
                # handle the case when no multiplication is defined on brackets are given eg. (34)4
                values.append(self.parse_exponent())
            else:
                break
        value = 1.0
        for factor in values:
            value *= factor
        return value


    def parse_parenthesis(self):
        self.skip_whitespace()
        char = self.peek()

        if char == '(':
            self.index += 1
            value = self.parse_expression()
            self.skip_whitespace()
            if self.peek() != ')':
                raise Exception("No closing parenthesis found at character " + str(self.index))
            self.index += 1
            return value
        else:
            return self.parse_negative()


    def parse_negative(self):
        self.skip_whitespace()
        char = self.peek()
        if char == '-':
            self.index += 1
            return -1 * self.parse_parenthesis()
        else:
            return self.parse_value()


    def parse_value(self):
        self.skip_whitespace()
        char = self.peek()
        if char in '0123456789':
            return self.parse_number()
        else:
            return self.parse_variable()


    def parse_variable(self):
        self.skip_whitespace()
        var = ''
        while self.has_next():
            char = self.peek()
            if char.lower() in '_abcdefghijklmnopqrstuvwxyz0123456789':
                var += char
                self.index += 1
            else:
                break

        value = self.vars.get(var,None)
        if value == None:
            raise Exception("Unrecognized variable '"+var+"'")
        return float(value)


    def parse_number(self):
        self.skip_whitespace()
        str_value = ''
        decimal_found = False
        char = ''

        while self.has_next():
            char = self.peek()
            if char == '.':
                if decimal_found:
                    raise Exception("Found an extra period in a number at character "+str(self.index) +"")
                decimal_found = True
                str_value += '.'
            elif char in '0123456789':
                str_value += char
            else:
                break
            self.index += 1

        if len(str_value) == 0:
            if char == '':
                raise Exception("Unexpected end found")
            else:
                raise Exception("Excepted number. Found "+ char)

        return float(str_value)



def evaluate(expression,vars={}):
    try:
        p = Parser(expression,vars)
        value = p.get_value()
    except Exception as ex:
        msg = ex.message
        raise Exception(msg)

    if int(value) == value:
        return int(value)

    epsilon = 0.0000000001
    if int(value + epsilon) != int(value):
        return int(value+epsilon)
    elif int(value-epsilon) != int(value):
        return int(value)
    return value

