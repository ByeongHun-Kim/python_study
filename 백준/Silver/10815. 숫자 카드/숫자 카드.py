import sys


N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))


cards.sort()
for check in checks:
    start, end = 0, N-1
    flag = False
    while end >= start:
        mid = (end + start) // 2
        if cards[mid] == check:
            flag = True
            break

        elif cards[mid] > check:
            end = mid - 1

        else:
            start = mid + 1

    if flag:
        print(1, end=" ")
    else:
        print(0, end=" ")
