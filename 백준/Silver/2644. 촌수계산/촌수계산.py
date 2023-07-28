from collections import deque
import sys
sys.setrecursionlimit(10**9)


N = int(sys.stdin.readline())
X, Y = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
    

def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)


visited[X] = 1
bfs(graph, X, visited)
print(visited[Y] - 1)