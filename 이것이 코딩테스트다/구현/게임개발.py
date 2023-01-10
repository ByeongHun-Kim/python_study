import sys

N, M = map(int, sys.stdin.readline().split())
x, y, direction = map(int, sys.stdin.readline().split())

map = []
for _ in range(N):
    map.append(list(map(int, sys.stdin.readline().split)))