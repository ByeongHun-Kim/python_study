import sys

N = int(sys.stdin.readline())

data = {}
for i in range(N):
    d = sys.stdin.readline().strip()
    if d in data:
        data[d] += 1
    else:
        data[d] = 1
    

print(sorted(data.items(), key=lambda x: (-x[1], x[0]))[0][0])