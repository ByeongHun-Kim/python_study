import sys

N, M, K = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort()
first = data[N-1]
second = data[N-2]

# 1
print((first * K + second) * (M//(K+1)) + first * (M % (K+1)))

# 2
result = 0
while 1:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1
print(result)
