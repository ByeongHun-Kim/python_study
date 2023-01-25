import sys


N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

sort_data = sorted(data)

for d in data:
    idx = sort_data.index(d)
    sort_data[sort_data.index(d)] = -1
    print(idx, end=" ")