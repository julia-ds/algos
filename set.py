# Implement a set using a hash table.
# Input data
# The input file contains descriptions of operations, their number does not exceed 1000000.
# Each line contains one of the following operations:
# insert 𝑥 — add element 𝑥 to the set. If the element is already in the set, then nothing needs to be done.
# delete 𝑥 - delete element 𝑥. If there is no element 𝑥, then nothing needs to be done.
# exists 𝑥 — if the key 𝑥 is in the set, output "true", if not, "false".
# Only integers that do not exceed 109 in absolute value are placed and removed from the set.
# Output
# Output sequentially the result of all operations exists. Follow the example output file format.
# Example
# input
# insert 2
# insert 5
# insert 3
# exists 2
# exists 4
# insert 2
# delete 2
# exists 2
# output
# true
# false
# false

import sys

SEPARATOR = "\n"
UNICODE = "utf-8"


class Set:
    def __init__(self):
        self.size = 2000007
        self.elements = [None] * self.size

    def hash_func(self, value):
        P = 10 ** 9 + 7
        A = 23
        return ((A * value) % P) % self.size

    def insert(self, value):
        i = self.hash_func(value)
        if self.elements[i] == value:
            return
        elif self.elements[i] == 'rip':
            self.elements[i] = value
        else:
            while self.elements[i] is not None and self.elements[i] != 'rip':
                i = (i + 1) % self.size
            self.elements[i] = value

    def exists(self, value):
        i = self.hash_func(value)
        while self.elements[i] is not None:
            if self.elements[i] == value:
                return 'true'
            i = (i + 1) % self.size
        return 'false'

    def delete(self, value):
        i = self.hash_func(value)
        while self.elements[i] is not None:
            if self.elements[i] == value:
                self.elements[i] = 'rip'
            i = (i + 1) % self.size


a = Set()

stdin = sys.stdin.readlines()
result = []
for e in stdin:
    operation, element = e.split(' ')
    if operation == 'insert':
        a.insert(int(element))
    elif operation == 'delete':
        a.delete(int(element))
    else:
        result.append(a.exists(int(element)))

sys.stdout.buffer.write(SEPARATOR.join(result).encode(UNICODE))