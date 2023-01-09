import sys

N, M = map(int, sys.stdin.readline().split())

cards = []

# 1
for i in range(N):
    card_list = list(map(int, sys.stdin.readline().split()))
    cards.append(min(card_list))

print(max(cards))

# 2
result = 0
for i in range(N):
    card_list = list(map(int, sys.stdin.readline().split()))
    result = max(result, min(card_list))

print(result)