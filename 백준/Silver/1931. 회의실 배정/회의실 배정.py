import sys
N = int(sys.stdin.readline())

data = []
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort(key=lambda x: (x[1], x[0]))
result = 1
end_time = data[0][1]
for i in range(1, N):
    if end_time <= data[i][0]:
        end_time = data[i][1]
        result += 1

print(result)