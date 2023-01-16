import sys


def dfs(x, y):
    global count
    if (x >= N) or (x < 0) or (y >= N) or (y < 0):
        return False

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


N = int(sys.stdin.readline().strip())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))


result = []
for i in range(N):
    for j in range(N):
        count = 0
        if dfs(i, j):
            result.append(count)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])