# Input
# The first line contains the number 𝑛 — the size of the array. (1≤𝑛≤500000) The second line contains 𝑛 numbers
# 𝑎𝑖 — elements of the array. The following is the description of operations, their number doesn't exceed 1000000.
# Each line contains one of the following operation:
# set 𝑖 𝑥 — set value 𝑥 to 𝑎[𝑖].
# sum 𝑖 𝑗 — print the sum of the elements in the array in the range from 𝑖 to 𝑗, it's guaranteed, that (1≤𝑖≤𝑗≤𝑛).
# All numbers in the input file and the results of all operations do not exceed 1018 in absolute value.
# Output
# Print successively all the operations sum. Follow the output file format from the example.
# Example
# input
# 5
# 1 2 3 4 5
# sum 2 5
# sum 1 5
# sum 1 4
# sum 2 4
# set 1 10
# set 2 3
# set 5 2
# sum 2 5
# sum 1 5
# sum 1 4
# sum 2 4
# output
# 14
# 15
# 10
# 9
# 12
# 22
# 20
# 10

import sys


def initialize_fenwick_tree(n, arr):
    fenwick_tree = [0] * (n + 1)
    for i in range(n):
        fenwick_tree = update_tree(fenwick_tree, n, i, arr[i])
    return fenwick_tree


def update_tree(fenwick_tree, n, i, value):
    i += 1
    while i <= n:
        fenwick_tree[i] += value
        i += i & (-i)
    return fenwick_tree


def get_sum(fenwick_tree, i):
    ans = 0
    i = i + 1
    while i > 0:
        ans += fenwick_tree[i]
        i -= i & (-i)
    return ans


def set_value(fenwick_tree, arr, n, i, x):
    value = x - arr[i]
    arr[i] = x
    fenwick_tree = update_tree(fenwick_tree, n, i, value)
    return arr, fenwick_tree


n = int(input())
arr = list(map(int, input().split(' ')))
fenwick_tree = initialize_fenwick_tree(n, arr)

result = []
stdin = sys.stdin.readlines()

for inp in stdin:
    inp = inp.split(' ')
    if inp[0] == 'sum':
        if int(inp[1]) > 1:
            result.append(get_sum(fenwick_tree, int(inp[2]) - 1) - get_sum(fenwick_tree, int(inp[1]) - 2))
        else:
            result.append(get_sum(fenwick_tree, int(inp[2]) - 1))
    else:
        arr, fenwick_tree = set_value(fenwick_tree, arr, n, int(inp[1]) - 1, int(inp[2]))

print(*result)