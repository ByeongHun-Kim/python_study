import sys
S = int(sys.stdin.readline())

N = 0
result = 0

while 1:
    N += 1
    result = N * (N + 1) / 2
    if result > S:
        N -= 1
        break

print(N)