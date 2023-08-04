import sys

N, K = map(int, sys.stdin.readline().split())

data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))

start, end = 1, max(data)
ans = 1

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for d in data:
        cnt += d // mid

    if cnt >= K:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1

print(ans)
