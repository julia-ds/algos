import sys
from collections import defaultdict
import heapq


def dijkstra(graph, start):
    dist = {v: float('Inf') for v in range(n)}
    dist[start] = 0
    queue = [(0, start)]
    while len(queue) > 0:
        next_w, next_v = heapq.heappop(queue)
        if next_w > dist[next_v]:
            continue
        for u, weight in graph[next_v].items():
            distance = next_w + weight
            if distance < dist[u]:
                dist[u] = distance
                heapq.heappush(queue, (distance, u))
    return dist


n, m = list(map(int, sys.stdin.readline().split(' ')))
graph = defaultdict(dict)
for _ in range(m):
    a, b, w = list(map(int, sys.stdin.readline().split(' ')))
    a -= 1
    b -= 1
    graph[a][b] = w
    graph[b][a] = w
answer = dijkstra(graph, 0)
for i in range(n):
    sys.stdout.write(str(answer[i]) + ' ')