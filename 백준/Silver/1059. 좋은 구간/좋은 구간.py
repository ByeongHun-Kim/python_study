import sys

L = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())

S.sort()
if n in S:
    print(0)

else:
    big = 0
    small = 0

    for s in S:
        if s < n:
            small = s

        elif (s > n) & (big == 0):
            big = s

    result = (n - small) * (big - n) - 1
    print(result)
