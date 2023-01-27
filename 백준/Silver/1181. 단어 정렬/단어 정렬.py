import sys


N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(sys.stdin.readline().strip())

data = list(set(data))
data.sort(key=lambda x: (len(x), x))

for d in data:
    print(d)