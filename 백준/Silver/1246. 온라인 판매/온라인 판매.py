import sys

N, M = map(int, sys.stdin.readline().split())

data = []
for i in range(M):
    data.append(int(sys.stdin.readline()))
data.sort()


price, gain = 0, 0
for idx, d in enumerate(data):
    if (len(data) - idx) > N:
        temp = d * N
    else:
        temp = d * (len(data) - idx)
    
    if temp > gain:
        gain = temp
        price = d

print(price, gain)