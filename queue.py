# You have to implement a queue with two operations:
# "+ x" — add an element 𝑥 to the queue;
# "-" — retrieve an element from the queue.
# For each retrieval operation output the result of the operation.
# Input
# The first line of the input contains the number of operations — 𝑛 (1≤𝑛≤10**5).
# Next 𝑛 lines contain the description of operations one per line. The added element cannot exceed 10**9.
# Output
# Output the results of all retrieve operations in the corresponding order, one per line.
# Example
# input
# 4
# + 1
# + 10
# -
# -
# output
# 1
# 10

class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.elements = [0] * self.capacity
        self.beg = -1
        self.end = -1

    def add(self, x):
        if (self.end + 1) % self.capacity == self.beg:
            self.ensure_capacity(2 * self.capacity, False)
        if self.beg == -1:
            self.beg = 0
            self.end = 0
            self.elements[self.end] = x
        else:
            self.end = (self.end + 1) % self.capacity
            self.elements[self.end] = x

    def ensure_capacity(self, new_capacity, remove):
        new_elements = [0] * new_capacity
        if remove:
            for i, el in enumerate(self.elements[self.beg: self.end + 1]):
                new_elements[i] = el
            self.elements = new_elements
            self.capacity = new_capacity
            self.end = self.end - self.beg
            self.beg = 0
        else:
            for i, el in enumerate(self.elements[self.beg: self.capacity] + self.elements[0: self.beg]):
                new_elements[i] = el
            self.elements = new_elements
            self.end = self.capacity - 1
            self.beg = 0
            self.capacity = new_capacity

    def erase(self):
        if 4 * (self.end - self.beg) == self.capacity:
            self.ensure_capacity(self.capacity // 2, True)
        if self.beg == self.end:
            erased_element = self.elements[self.beg]
            self.beg = -1
            self.end = -1
            return erased_element
        else:
            erased_element = self.elements[self.beg]
            self.beg = (self.beg + 1) % self.capacity
            return erased_element


queue = DynamicArray()

n = int(input())
for i in range(n):
    input_data = list(map(str, input().split(' ')))
    if input_data[0] == '+':
        queue.add(input_data[1])
    elif input_data[0] == '-':
        print(queue.erase())