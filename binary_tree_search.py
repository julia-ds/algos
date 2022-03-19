# Implement a simple binary search tree.
# Input data
# The input file contains a description of tree operations, their number does not exceed 100.
# Each line contains one of the following operations:
# insert 𝑥 — add key 𝑥 to the tree. If the key 𝑥 is in the tree, then nothing needs to be done;
# delete 𝑥 — remove the key 𝑥 from the tree. If there is no key 𝑥 in the tree, then nothing needs to be done;
# exists 𝑥 — if the key 𝑥 exists in the tree, output "true", if not, "false";
# next 𝑥 - print the minimum element in the tree strictly greater than 𝑥, or "none" if there is none;
# prev 𝑥 - print the maximum element in the tree strictly less than 𝑥, or "none" if there is none.
# Only integers that do not exceed 109 in absolute value are inserted and extracted into the tree.
# Output
# Output sequentially the result of all operations exists, next, prev. Follow the example output file format.
# Example
# input
# insert 2
# insert 5
# insert 3
# exists 2
# exists 4
# next 4
# prev 4
# delete 5
# next 4
# prev 4
# output
# true
# false
# 5
# 3
# none
# 3

import sys


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(v, x):
    if v is None:
        return TreeNode(x)
    elif x < v.key:
        v.left = insert(v.left, x)
    elif x > v.key:
        v.right = insert(v.right, x)
    return v


def delete(v, x):
    if v is None:
        return None
    elif x < v.key:
        v.left = delete(v.left, x)
    elif x > v.key:
        v.right = delete(v.right, x)
    elif v.right is None and v.left is None:
        return None
    elif v.left is None:
        v = v.right
    elif v.right is None:
        v = v.left
    else:
        v.key = find_max(v.left).key
        v.left = delete(v.left, v.key)
    return v


def find_max(v):
    while v.right is not None:
        v = v.right
    return v


def next(v, x):
    root = v
    res = None
    while root is not None:
        if root.key > x:
            res = root.key
            root = root.left
        else:
            root = root.right
    return res


def prev(v, x):
    root = v
    res = None
    while root is not None:
        if root.key < x:
            res = root.key
            root = root.right
        else:
            root = root.left
    return res


def exists(v, x: int):
    if v is None:
        return False
    else:
        if v.key == x:
            return True
        elif x < v.key:
            return exists(v.left, x)
        else:
            return exists(v.right, x)


bst = None
stdin = sys.stdin.readlines()
for inp in stdin:
    inp = inp.split(' ')
    if inp[0] == 'insert':
        bst = insert(bst, int(inp[1]))
    elif inp[0] == 'delete':
        bst = delete(bst, int(inp[1]))
    elif inp[0] == 'exists':
        sys.stdout.write(str(exists(bst, int(inp[1]))).lower() + '\n')
    elif inp[0] == 'next':
        sys.stdout.write(str(next(bst, int(inp[1]))).lower() + '\n')
    else:
        sys.stdout.write(str(prev(bst, int(inp[1]))).lower() + '\n')
