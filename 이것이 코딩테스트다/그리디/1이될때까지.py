import sys

N, K = map(int, sys.stdin.readline().split())

result = 0
while True:
    if N == 1:
        break

    if N % K == 0:
        N = N / K
    else:
        N -= 1

    result += 1
print(result)

N, K = map(int, sys.stdin.readline().split())
result = 0
while True:
    target = (N // K) * K
    result += N - target
    N = target
    if N < K:
        result += (N-1)
        break

    N //= K
    result += 1
print(result)
