# For a given connected undirected graph find a spanning tree with minimum weight.
# Input
# First line of input consists of two integers 𝑛 and 𝑚 — number of vertices and edges, respectively (2≤𝑛≤200000,1≤𝑚≤200000).
# Next 𝑚 lines describe edges one per line in the following format: three integers 𝑏𝑖, 𝑒𝑖 and 𝑤𝑖 — ends and the weight
# of the edge 𝑖, respectively (1≤𝑏𝑖,𝑒𝑖≤𝑛, 0≤𝑤𝑖≤100000).
# "Everything is connected" © D.G (Graph is too, by the way:)
# Output
# Output a single integer — minimum weight of the spanning tree.
# Example
# input
# 4 4
# 1 2 1
# 2 3 2
# 3 4 5
# 4 1 4
# output
# 7

import sys


class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def get(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.get(self.parent[x])
        return self.parent[x]

    def join(self, x, y):
        x = self.get(x)
        y = self.get(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.parent[x] = y


n, m = list(map(int, sys.stdin.readline().split(" ")))
edge = []
for _ in range(m):
    b, e, w = list(map(int, sys.stdin.readline().split(" ")))
    if b != e:
        edge.append([w, b - 1, e - 1])
edge = sorted(edge)
snm = Disjoint(n)
dist = 0
for w, b, e in edge:
    if snm.get(b) != snm.get(e):
        dist += w
        snm.join(b, e)
sys.stdout.write(str(dist))





