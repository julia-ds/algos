# Your task is to maintain DSU. Moreover, you'll have to find minimum and maximum element and number of elements in the subset.
# Initially, each element is in it's own subset.
# Input
# First line of input consists of a single integer n — number of elements in set (1≤n≤300000).
# Each of the next lines contains a single operation. For each of operation get, you should output minimum and maximum
# element and number of elements in corresponding subset.
# Output
# Output the sequence of results of operations get.
# Example
# input
# 5
# union 1 2
# get 3
# get 2
# union 2 3
# get 2
# union 1 3
# get 5
# union 4 5
# get 5
# union 4 1
# get 5
# output
# 3 3 1
# 1 2 2
# 1 3 3
# 5 5 1
# 4 5 2
# 1 5 5

import sys


class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.min = [i for i in range(n)]
        self.max = [i for i in range(n)]
        self.count = [1 for _ in range(n)]

    def get(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        x = self.get(x)
        y = self.get(y)
        min_x, max_x, count_x = self.min[x], self.max[x], self.count[x]
        min_y, max_y, count_y = self.min[y], self.max[y], self.count[y]
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.parent[x] = y
        self.min[y] = min(min_x, min_y)
        self.max[y] = max(max_x, max_y)
        self.count[y] = count_x + count_y


n = int(sys.stdin.readline())
snm = Disjoint(n)
while True:
    inp = sys.stdin.readline().split(" ")
    if inp[0] == "union":
        snm.join(int(inp[1]) - 1, int(inp[2]) - 1)
    elif inp[0] == "get":
        x = snm.get(int(inp[1]) - 1)
        sys.stdout.write(str(snm.min[x] + 1) + " ")
        sys.stdout.write(str(snm.max[x] + 1) + " ")
        sys.stdout.write(str(snm.count[x]) + "\n")
    else:
        break