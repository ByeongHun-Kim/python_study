import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort()

result = 0
for idx, i in enumerate(P):
    result += (N - idx) * i
print(result)
