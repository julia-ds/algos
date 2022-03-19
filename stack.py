# In a postfix notation (Reverse Polish notation), two operands are followed by an operation.
# For example, the sum of two numbers A and B is written as A B +.
# The expression B C + D * means (B + C) * D, and the expression A B C + D * + means A + (B + C) * D.
# The advantage of a postfix notation is that it does not require brackets and additional operator precedence agreements
# for its reading.
# An expression is given in the reverse Polish notation. Calculate the result.
# Input
# The input contains the expression in the postfix notation containing single-digit numbers and the operations +, -, *.
# The string contains no more than 100 numbers and operations.
# Output
# Output the result of the expression. It is guaranteed that the result of the expression, as well as the results of
# all intermediate calculations is less than 231 by an absolute value.
# Example
# input
# 8 9 + 1 7 - *
# output
# -102

class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.elements = [0] * self.capacity

    def add(self, x, ind):
        if self.size == self.capacity:
            self.ensure_capacity(2 * self.capacity)
        for i in range(self.size - 1, ind - 1, -1):
            self.elements[i + 1] = self.elements[i]
        self.elements[ind] = x
        self.size += 1

    def ensure_capacity(self, new_capacity):
        new_elements = [0] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity

    def erase(self, ind):
        if 4 * self.size == self.capacity:
            self.ensure_capacity(self.capacity // 2)
        if ind == self.size - 1:
            self.elements[ind] = 0
            self.size -= 1
            return
        for i in range(ind, self.size - 1):
            self.elements[i] = self.elements[i + 1]
        self.elements[self.size - 1] = 0
        self.size -= 1


class Stack:
    def __init__(self):
        self.stack = DynamicArray()

    def push(self, value):
        self.stack.add(value, 0)

    def pop(self):
        erased_value = self.stack.elements[0]
        self.stack.erase(0)
        return erased_value

    def math(self, math_operator):
        fisrt = self.pop()
        second = self.pop()
        if math_operator[0] == '+':
            self.push(second + fisrt)
        elif math_operator[0] == '-':
            self.push(second - fisrt)
        else:
            self.push(second * fisrt)


stack = Stack()
input_data = list(map(str, input().split(' ')))

for element in input_data:
    if element == '+' or element == '-' or element == '*':
        stack.math(element)
    else:
        stack.push(int(element))

print(stack.stack.elements[0])