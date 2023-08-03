import sys


while True:
    N, M = map(int, sys.stdin.readline().split())
    if (N == 0) and (M == 0):
        break

    A = [int(sys.stdin.readline()) for _ in range(N)]
    B = [int(sys.stdin.readline()) for _ in range(M)]

    ans = 0
    for b in B:
        start = 0
        end = N-1

        while start <= end:
            mid = (start + end) // 2
            if A[mid] == b:
                ans += 1
                break

            elif A[mid] < b:
                start = mid + 1

            else:
                end = mid - 1

    print(ans)