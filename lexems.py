# A numeric expression was specified that ends with a dot. It is necessary to break it into tokens and print each one
# on a new line. It is guaranteed that the original expression is correct.
# The expression can contain signs of addition, subtraction, multiplication, and brackets. The priority of operations
# is standard. All numbers in the expression are integers and belong to the LongInt range.
# Input data
# The first line contains the given expression. Its length does not exceed 100 characters. It is guaranteed that the
# expression ends with a dot.
# Output
# Print all occurring tokens of the expression in order and exactly one on each line.
# Example
# input
# 1+(2*2-3).
# output
# 1
# +
# (
# 2
# *
# 2
# -
# 3
# )

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


def main():
    sequence = sys.stdin.readline().strip()
    lexer = Lexer(sequence)
    while not lexer.last:
        sys.stdout.write(str(lexer.next_token()) + '\n')


if __name__ == '__main__':
    main()