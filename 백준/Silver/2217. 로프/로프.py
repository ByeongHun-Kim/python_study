import sys
N = int(sys.stdin.readline())

data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))

data.sort(reverse=True)
for i in range(N):
    data[i] = data[i] * (i + 1)

print(max(data))