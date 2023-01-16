import sys
from collections import deque


def bfs():
    queue = deque([1])
    visited[1] = True
    result = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                result += 1
    return result


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    h, t = map(int, sys.stdin.readline().split())
    graph[h].append(t)
    graph[t].append(h)
print(bfs())
