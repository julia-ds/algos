# You are given a directed weighted graph. Please find the negative cycle, or answer that it does not exist.
# Input
# The first line of the input contains one integer n (1≤n≤100) — the number of vertices. Next n lines contain n integers
# each and represent an adjacency matrix with weights. The weights do not exceed 10000 in absolute value.
# If there is no edge, the corresponding weight is equal to 100000.
# Output
# The first line of the output should contain "YES", if the cycle exists, or "NO", otherwise. If the cycle exists the
# second line should contain the number of vertices in the cycle, and the third line should contain the vertices in
# the order of the cycle.
# Example
# input
# 2
# 0 -1
# -1 0
# output
# YES
# 2
# 2 1

import sys

MAX_W = 100000


def floyd(d, n):
    graph = d[:]
    next = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            next[i][j] = j
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if graph[u][v] > graph[u][k] + graph[k][v]:
                    graph[u][v] = graph[u][k] + graph[k][v]
                    next[u][v] = next[u][k]
    return next, graph


n = int(sys.stdin.readline())
adjacency_matrix = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split(' ')))
    row = [float('Inf') if x == MAX_W else x for x in row]
    adjacency_matrix.append(row)
next, d = floyd(adjacency_matrix, n)
negative_cycle = False
for i in range(n):
    if d[i][i] < 0:
        negative_cycle = True
        start = i
        break
if not negative_cycle:
    sys.stdout.write('NO' + '\n')
else:
    sys.stdout.write('YES' + '\n')
    cur = next[start][start]
    answer = [cur]
    while cur != start:
        cur = next[cur][start]
        if cur in answer:
            start = cur
            cur = next[start][start]
            answer = [cur]
        else:
            answer.append(cur)
    sys.stdout.write(str(len(answer)) + '\n')
    for ans in answer:
        sys.stdout.write(str(ans + 1) + ' ')