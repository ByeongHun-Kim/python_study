import sys
from collections import deque


def dfs(graph, start, visited):
    print(start, end=" ")
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    h, t = map(int, sys.stdin.readline().split())
    graph[h].append(t)
    graph[t].append(h)

for g in graph:
    g.sort()

dfs(graph, V, [False]*(N+1))
print()
bfs(graph, V, [False]*(N+1))