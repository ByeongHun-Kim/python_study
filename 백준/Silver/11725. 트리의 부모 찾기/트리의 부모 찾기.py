import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]


def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            result[i] = start
            dfs(i)


dfs(1)
for i in range(2, N+1):
    print(result[i])