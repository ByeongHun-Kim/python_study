from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


max_size = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    global max_size
    size = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                size += 1
                queue.append((nx, ny))

    if size > max_size:
        max_size = size


result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result += 1
            bfs(i, j)

print(result)
print(max_size)
