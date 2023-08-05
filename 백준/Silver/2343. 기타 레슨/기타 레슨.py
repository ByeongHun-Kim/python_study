import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start, end = max(arr), sum(arr)
ans = 0

while start <= end:
    mid = (start + end) // 2

    cnt, temp = 0, 0
    for i in range(N):
        if temp + arr[i] > mid:
            temp = 0
            cnt += 1
        temp += arr[i]

    if temp:
        cnt += 1

    if cnt > M:
        start = mid + 1

    else:
        ans = mid
        end = mid - 1

print(ans)
