# Given points on the plane that are vertices of the complete graph. The weight of an edge is equal to the distance
# between the points corresponding to the ends of this edge. It is required in this graph to find a spanning tree of
# minimum weight.
# Input data
# The first line of the input file contains a natural number 𝑛 — the number of graph vertices (1≤𝑛≤10000).
# Each of the following 𝑛 lines contains two integers 𝑥𝑖, 𝑦𝑖 — the coordinates of the 𝑖-th vertex (−10000≤𝑥𝑖,𝑦𝑖≤10000).
# No two points match.
# Output
# The first line of the output file must contain one real number — the weight of the minimum spanning tree.
# Example
# Input
# 2
# 0 0
# 1 1
# Output
# 1.4142135624

import sys


def prim(v, n):
    used = {_: False for _ in range(n)}
    dist = {_: float('Inf') for _ in range(n)}
    dist[0] = 0
    next_v = -1
    mst = 0
    for _ in range(n):
        min_weight = float('Inf')
        for ind in range(n):
            if next_v == -1 or ((not used[ind]) and (dist[ind] < min_weight)):
                min_weight = dist[ind]
                next_v = ind
        for i in range(n):
            new_root = ((v[i][0] - v[next_v][0]) ** 2 +
                        (v[i][1] - v[next_v][1]) ** 2)
            dist[i] = min(dist[i], new_root)
        mst += min_weight ** 0.5
        used[next_v] = True
    return mst


n = int(sys.stdin.readline())
v = []
for _ in range(n):
    xy = list(map(int, sys.stdin.readline().split(" ")))
    v.append(xy)
sys.stdout.write(str(prim(v, n)))
