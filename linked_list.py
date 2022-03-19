# You have to implement the data structure that supports the following operations:
# 1 𝑥 — add 𝑥 to an end of the data structure.
# 2 — retrieve the last element from the data structure.
# 3 — find the minimal element in the data structure.
# Input
# The first line of the input contains one integer 𝑛 (1≤𝑛≤106) — the number of operations.
# Next 𝑛 lines contain the description of operations, one per line.
# The argument 𝑥 in an operation of the first type lies in [−109,109]).
# It is guaranteed that before retrieval the data structure is not empty.
# Output
# Output the result for each operation of the third type, one per line.
# Example
# input
# 8
# 1 2
# 1 3
# 1 -3
# 3
# 2
# 3
# 2
# 3
# output
# -3
# 2
# 2

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.min = None

    def push(self, value):
        if self.size == 0:
            self.head = Node(value)
            self.tail = self.head
            self.min = value
        elif value < self.min:
            dummy = 2 * value - self.min
            new_node = Node(dummy)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None
            self.min = value
        else:
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None
        self.size += 1

    def pop(self):
        if self.size == 1:
            self.head = None
            self.tail = self.head
            self.min = None
        else:
            if self.tail.value <= self.min:
                self.min = 2 * self.min - self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def print_min(self):
        return self.min


stack = LinkedList()

n = int(input())
for i in range(n):
    input_data = list(map(int, input().split(' ')))
    if input_data[0] == 1:
        stack.push(input_data[1])
    elif input_data[0] == 2:
        stack.pop()
    else:
        print(stack.min)