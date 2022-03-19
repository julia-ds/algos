# Implement a stitched associative array using a hash table.
#
# Input data
# The input file contains descriptions of operations, their number does not exceed 100000.
# Each line contains one of the following operations:
# put 𝑥 𝑦 — put the key 𝑥 in correspondence with the value 𝑦.
# If the element already exists, then the value must be changed.
# delete 𝑥 — delete key 𝑥. If there is no element 𝑥, then nothing needs to be done.
# get 𝑥 — if the key 𝑥 is in the set, print the value corresponding to it, if not, print "none".
# prev 𝑥 - output the value corresponding to the key in the associative array, which was inserted last,
# but before 𝑥 or "none" if there is no such key or there is no 𝑥 in the array.
# next 𝑥 - display the value corresponding to the key in the associative array that was inserted before everyone else,
# but after 𝑥 or "none" if there is none or there is no 𝑥 in the array.
# Keys and values are strings of Latin letters with a maximum length of 20 characters.
# Output
# Print successively the result of all get, prev, next operations. Follow the example output file format.
# Example
# Input
# put zero a
# put one b
# put two c
# put three d
# put four e
# get two
# prev two
# next two
# delete one
# delete three
# get two
# prev two
# next two
# next four
# Output
# c
# b
# d
# c
# a
# e
# none

import sys

SEPARATOR = "\n"
UNICODE = "utf-8"


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.map_next = None
        self.map_prev = None


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
            deleted_node = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
                self.size = 0
            return deleted_node
        previous_node = self.head
        node = self.head
        while node.next is not None:
            node = node.next
            if node.key == remove_key:
                deleted_node = node
                previous_node.next = node.next
                if node.next is None:
                    self.tail = previous_node
                self.size -= 1
                return deleted_node
            previous_node = node
        return None


class Map:
    def __init__(self):
        self.size = 100003
        self.elements = [LinkedList() for _ in range(self.size)]
        self.map_last = Node(None, 'none')

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
            new_node = Node(key, value)
            new_node.map_prev = self.map_last
            self.map_last.map_next = new_node
            self.map_last = new_node
            self.elements[hash_key].push(new_node)
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
        new_node = Node(key, value)
        new_node.map_prev = self.map_last
        self.map_last.map_next = new_node
        self.map_last = new_node
        self.elements[hash_key].push(new_node)
        return

    def delete(self, remove_key):
        hash_key = self.hash_func(remove_key)
        if self.elements[hash_key].head is None:
            return
        else:
            deleted_node = self.elements[hash_key].pop(remove_key)
            if deleted_node is None:
                pass
            elif deleted_node.map_next is None:
                self.map_last = deleted_node.map_prev
                deleted_node.map_prev.map_next = None
            else:
                deleted_node.map_prev.map_next = deleted_node.map_next
                deleted_node.map_next.map_prev = deleted_node.map_prev
            return

    def get(self, key):
        hash_key = self.hash_func(key)
        if self.elements[hash_key].head is None:
            return None
        elif self.elements[hash_key].head.key == key:
            return self.elements[hash_key].head
        else:
            node = self.elements[hash_key].head
            while node.next is not None:
                node = node.next
                if node.key == key:
                    return node
            return None


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
    else:
        printed_node = a.get(inp[1])
        if printed_node is None:
            result.append('none')
        elif inp[0] == 'next':
            if printed_node.map_next is None:
                result.append('none')
            else:
                result.append(str(printed_node.map_next.value))
        elif inp[0] == 'prev':
            if printed_node.map_prev is None:
                result.append('none')
            else:
                result.append(str(printed_node.map_prev.value))
        elif inp[0] == 'get':
            result.append(str(printed_node.value))

sys.stdout.buffer.write(SEPARATOR.join(result).encode(UNICODE))