import sys

N = int(sys.stdin.readline())
D = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

D.sort()
ans = 0
start = 1
end = D[-1]
while start <= end:
    mid = (start + end) // 2
    m = 0
    for d in D:
        if d > mid:
            m += mid
        else:
            m += d

    if m > M:
        end = mid - 1

    else:
        ans = mid
        start = mid + 1

print(ans)