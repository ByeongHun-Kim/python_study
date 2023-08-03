import sys


while True:
    N, M = map(int, sys.stdin.readline().split())
    if (N == 0) and (M == 0):
        break

    A = {}
    for i in range(N):
        A[int(sys.stdin.readline())] = 1

    result = 0

    for i in range(M):
        target = int(sys.stdin.readline())
        if target in A:
            result += 1
    print(result)
