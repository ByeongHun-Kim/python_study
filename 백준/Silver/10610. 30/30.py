import sys
N = list(map(int, sys.stdin.readline().strip()))

if 0 not in N:
    print(-1)

elif sum(N) % 3 != 0:
    print(-1)

else:
    N.sort(reverse=True)
    print("".join(map(str, N)))