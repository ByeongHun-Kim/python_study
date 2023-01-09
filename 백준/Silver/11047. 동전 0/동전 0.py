import sys
N, K = map(int, sys.stdin.readline().split())

result = 0
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)

for coin in coins:
    if K < coin:
        continue
    result += (K // coin)
    K %= coin

print(result)