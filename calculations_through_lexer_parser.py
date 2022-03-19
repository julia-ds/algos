# A numeric expression was specified that ends with a dot. You must calculate its value or say that it contains an error.
# The expression can contain signs of addition, subtraction, multiplication, and brackets.
# The priority of operations is standard. All numbers in the expression are integers and belong to the LongInt range.
# It is also guaranteed that all intermediate calculations fit into this type. Unary plus and unary minus cannot occur
# in an expression, as well as two characters in a row.
# Input data
# The first line contains the given expression. Its length does not exceed 100 characters. It is guaranteed that the
# expression ends with a dot.
# Output
# Print the value of this expression or the word "WRONG" if the value is not defined.
# Examples
# input
# 1+(2*2-3).
# output
# 2
# input
# 1+a+1.
# output
# WRONG

import sys

NUMBERS = {str(e) for e in range(0, 10)}
SYMBOLS = {'+', '-', '*', '(', ')'}
EOF = '.'


class Lexer:
    def __init__(self, word):
        self.word = word
        self.cur = 0
        self.last = False

    def next_token(self):
        element = self.word[self.cur]
        if element in NUMBERS:
            result = ''
            while element in NUMBERS:
                result += element
                self.cur += 1
                element = self.word[self.cur]
            self.cur -= 1
        elif element in SYMBOLS:
            result = element
        else:
            self.last = True
            result = ''
        self.cur += 1
        return result


class Parser:
    def __init__(self, lexer):
        self.tokens = []
        self.cur = 0
        while not lexer.last:
            self.tokens.append(lexer.next_token())
        self.size = len(self.tokens)

    def parse(self):
        result = self.parse_operation()
        if self.cur != self.size - 1:
            raise ValueError()
        return result

    def parse_operation(self):
        first_num = self.parse_multiplication()
        while self.cur < self.size:
            operation = self.tokens[self.cur]
            if operation == '+' or operation == '-':
                self.cur += 1
            else:
                break
            second_num = self.parse_multiplication()
            if operation == '+':
                first_num += second_num
            else:
                first_num -= second_num
        return first_num

    def parse_multiplication(self):
        first_num = self.parse_bracket()
        while self.cur < self.size:
            operation = self.tokens[self.cur]
            if operation == '*':
                self.cur += 1
            else:
                break
            second_num = self.parse_bracket()
            first_num *= second_num
        return first_num

    def parse_bracket(self):
        current_token = self.tokens[self.cur]
        if current_token == '(':
            self.cur += 1
            result = self.parse_operation()
            if self.cur == self.size:
                raise ValueError()
            next_token = self.tokens[self.cur]
            if next_token != ')':
                raise ValueError()
        else:
            result = int(current_token)
        self.cur += 1
        return result


def main():
    sequence = sys.stdin.readline().strip()
    lexer = Lexer(sequence)
    parser = Parser(lexer)
    try:
        sys.stdout.write(str(parser.parse()))
    except ValueError:
        sys.stdout.write('WRONG')


if __name__ == '__main__':
    main()