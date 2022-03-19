# On a N×N chessboard in square (x1,y1) there is a chess knight. He wants to get to square (x2,y2).
# What is the minimum number of moves he needs to do?
# Input
# Input contains five integers: N,x1,y1,x2,y2 (5≤N≤20,1≤x1,y1,x2,y2≤N). The top left square of the board has coordinates
# (1,1), the bottom right one is (N,N).
# Output
# In the first line output number K, the minimum number of knight's moves. Each of the following K lines must contain
# 2 numbers, the coordinates of the next cell in the path.
# Example
# input
# 5
# 1 1
# 3 2
# output
# 2
# 1 1
# 3 2

import sys


def bfs(graph, beginning, end, used):
    d = {beginning: beginning}
    queue = [beginning]
    used[beginning] = True
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            if not used[u]:
                used[u] = True
                queue.append(u)
                d[u] = v
                if u == end:
                    return d


def knight_moves(i, j, n):
    ans = []
    possible_moves = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]
    for move in possible_moves:
        i_new = i + move[0]
        j_new = j + move[1]
        if 0 <= i_new < n and 0 <= j_new < n:
            k = i_new * n + j_new
            ans.append(k)
    return ans


n = int(sys.stdin.readline())
beginning_i, beginning_j = list(map(int, sys.stdin.readline().split(' ')))
end_i, end_j = list(map(int, sys.stdin.readline().split(' ')))
beginning = (beginning_i - 1) * n + (beginning_j - 1)
end = (end_i - 1) * n + (end_j - 1)
k = -1
adjacency_lst = [[] for _ in range(n ** 2)]
for i in range(n):
    for j in range(n):
        k += 1
        adjacency_lst[k] = knight_moves(i, j, n)

used = {i: False for i in range(n ** 2)}
hist_dict = bfs(adjacency_lst, beginning, end, used)
result = []
k = end
while k != beginning:
    result.append((int(k / n), k % n))
    k = hist_dict[k]
result.append((int(beginning / n), beginning % n))

sys.stdout.write(str(len(result)) + '\n')
for a in reversed(result):
    sys.stdout.write(f'{a[0] + 1} {a[1] + 1}' + '\n')