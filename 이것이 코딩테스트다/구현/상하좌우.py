import sys

N = int(sys.stdin.readline())
moves = sys.stdin.readline().split()

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ["L", "R", "U", "D"]

for move in moves:
    for i in range(len(move_type)):
        if move == move_type[i]:
            x_temp = x + dx[i]
            y_temp = y + dy[i]

    if (x_temp < 1) or (x_temp > N) or (y_temp < 1) or (y_temp > N):
        continue

    x, y = x_temp, y_temp

print(x, y)