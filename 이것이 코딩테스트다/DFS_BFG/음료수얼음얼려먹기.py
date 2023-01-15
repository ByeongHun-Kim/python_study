import sys

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))


def dfs(x, y):
    if (x < 0) or (x >= N) or (y < 0) or (y >= M):
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for n in range(N):
    for m in range(M):
        if dfs(n, m) is True:
            result += 1

print(result)