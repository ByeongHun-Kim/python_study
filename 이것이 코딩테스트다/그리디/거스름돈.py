import sys

N = int(sys.stdin.readline())

coin_type = [500, 100, 50, 10]
result = []

for coin in coin_type:
    result.append(N//coin)
    N = N % coin

print(result)
