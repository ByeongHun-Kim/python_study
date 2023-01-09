import sys
N = int(sys.stdin.readline())

data = []
for i in range(2):
    data.append(list(map(int, sys.stdin.readline().split())))

data[0].sort()
data[1].sort(reverse=True)

result = 0
for i in range(N):
    result += data[0][i] * data[1][i]
print(result)