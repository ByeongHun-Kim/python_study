import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if (temp_x < 0) or (temp_x >= N) or (temp_y < 0) or (temp_y >= M):
                continue

            if graph[temp_x][temp_y] == 0:
                continue

            if graph[temp_x][temp_y] == 1:
                graph[temp_x][temp_y] = graph[x][y] + 1
                print(graph)
                queue.append((temp_x, temp_y))
    return graph[N-1][M-1]


print(bfs(0, 0))
