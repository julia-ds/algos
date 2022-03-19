# Implement an associative array using a hash table.
# Input data
# The input file contains descriptions of operations, their number does not exceed 100000.
# Each line contains one of the following operations:
# put 𝑥 𝑦 — put the key 𝑥 in correspondence with the value 𝑦. If the key already exists, then the value must be changed.
# delete 𝑥 — delete key 𝑥. If there is no element 𝑥, then nothing needs to be done.
# get 𝑥 — if the key 𝑥 is in the associative array, then print the corresponding value, otherwise print "none".
# Keys and values are strings of Latin letters with a maximum length of 20 characters.
# Output
# Print the result of all get operations in sequence. Follow the example output file format.
# Example
# Input
# put hello privet
# put bye poka
# get hello
# get bye
# delete hello
# get hello
# Output
# privet
# poka
# none

import sys

SEPARATOR = "\n"
UNICODE = "utf-8"


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = None
        self.size += 1

    def pop(self, remove_key):
        if self.head.key == remove_key:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
                self.size = 0
            return
        previous_node = self.head
        node = self.head
        while node.next is not None:
            node = node.next
            if node.key == remove_key:
                previous_node.next = node.next
                if node.next is None:
                    self.tail = previous_node
                self.size -= 1
                return
            previous_node = node
        return


class Map:
    def __init__(self):
        self.size = 100003
        self.elements = [LinkedList() for _ in range(self.size)]

    def hash_func(self, value):
        P = 10 ** 9 + 7
        A = 29
        a_pow = 83
        res = 0
        for i, symbol in enumerate(reversed(value)):
            res = ((ord(symbol) * a_pow) % P + res) % P
            a_pow = (a_pow * A) % P
        return res % self.size

    def put(self, key, value):
        hash_key = self.hash_func(key)
        if self.elements[hash_key].head is None:
            self.elements[hash_key].push(Node(key, value))
            return
        elif self.elements[hash_key].head.key == key:
            self.elements[hash_key].head.value = value
            return
        else:
            node = self.elements[hash_key].head
            while node.next is not None:
                node = node.next
                if node.key == key:
                    node.value = value
                    return
        self.elements[hash_key].push(Node(key, value))

    def delete(self, remove_key):
        hash_key = self.hash_func(remove_key)
        if self.elements[hash_key].head is None:
            return
        else:
            self.elements[hash_key].pop(remove_key)
            return

    def get(self, key):
        hash_key = self.hash_func(key)
        if self.elements[hash_key].head is None:
            return 'none'
        elif self.elements[hash_key].head.key == key:
            return str(self.elements[hash_key].head.value)
        else:
            node = self.elements[hash_key].head
            while node.next is not None:
                node = node.next
                if node.key == key:
                    return str(node.value)
            return 'none'


a = Map()

stdin = sys.stdin.readlines()
result = []
for inp in stdin:
    inp = inp.split(' ')
    inp = [val.strip() for val in inp]
    if inp[0] == 'put':
        a.put(inp[1], inp[2])
    elif inp[0] == 'delete':
        a.delete(inp[1])
    elif inp[0] == 'get':
        result.append(a.get(inp[1]))

sys.stdout.buffer.write(SEPARATOR.join(result).encode(UNICODE))