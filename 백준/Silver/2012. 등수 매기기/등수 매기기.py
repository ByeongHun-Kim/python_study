import sys

N = int(sys.stdin.readline())

A = []
for i in range(N):
    A.append(int(sys.stdin.readline()))
A.sort()

print(sum([a - (i + 1) if (a - (i + 1)) >
      0 else i + 1 - a for i, a in enumerate(A)]))