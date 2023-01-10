import sys

data = sys.stdin.readline()
row = int(data[1])
col = int(ord(data[0])) - int(ord("a")) + 1

steps = [(-2, -1), (-1, -2), (-2, 1), (2, -1), (1, -2), (-1, 2), (2, 1), (1, 2)]

count = 0
for step in steps:
    x_temp = row + step[0]
    y_temp = col + step[1]

    if (x_temp < 1) or (x_temp > 8) or (y_temp < 1) or (y_temp > 8):
        continue

    count += 1

print(count)