import sys
from collections import deque


dx = [1, 1, 1, -1, 0, 0, -1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def bfs(x, y):
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if temp_x < 0 or temp_x >= N or temp_y < 0 or temp_y >= M:
                continue

            if graph[temp_x][temp_y] == 0:
                continue

            queue.append((temp_x, temp_y))
            graph[temp_x][temp_y] = 0


while True:
    M, N = map(int, sys.stdin.readline().split())
    visited = [[0 for i in range(M)] for j in range(N)]

    if N == 0 and M == 0:
        break

    graph = []
    for _ in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    result = 0
    for n in range(N):
        for m in range(M):
            if graph[n][m] == 1:
                bfs(n, m)
                result += 1

    print(result)