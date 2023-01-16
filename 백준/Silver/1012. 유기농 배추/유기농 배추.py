import sys
from collections import deque


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if temp_x < 0 or temp_x >= N or temp_y < 0 or temp_y >= M:
                continue

            if graph[temp_x][temp_y] == 0:
                continue

            graph[temp_x][temp_y] = 0
            queue.append((temp_x, temp_y))


T = int(sys.stdin.readline().strip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0 for i in range(M)] for j in range(N)]
    for i in range(K):
        m, n = map(int, sys.stdin.readline().split())
        graph[n][m] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                bfs(i, j)
                result += 1

    print(result)