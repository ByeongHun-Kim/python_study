import sys
from collections import deque


def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append([x, y])
    graph[x][y] = True
    result = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if temp_x < 0 or temp_x >= N or temp_y < 0 or temp_y >= M:
                continue

            if graph[temp_x][temp_y]:
                continue

            graph[temp_x][temp_y] = True
            queue.append([temp_x, temp_y])
            result += 1
    return result


M, N, K = map(int, sys.stdin.readline().split())
graph = [[False for m in range(M)] for n in range(N)]
data = []


for i in range(K):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            if not graph[x][y]:
                graph[x][y] = True


res = []
for n in range(N):
    for m in range(M):
        if not graph[n][m]:
            res.append(bfs(n, m))

res.sort()
print(len(res))
for r in res:
    print(r, end=" ")
