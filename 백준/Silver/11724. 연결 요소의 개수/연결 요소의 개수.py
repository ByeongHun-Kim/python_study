import sys
from collections import deque


def bfs(start):
    visited[start] = True
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)


for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


result = 0
for n in range(1, N+1):
    if not visited[n]:
        if not graph[n]:
            visited[n] = True
            result += 1
        else:
            bfs(n)
            result += 1

print(result)