import sys
N = int(sys.stdin.readline().strip())

for _ in range(N):
    x = sys.stdin.readline().strip()
    count = 0
    flag = True
    for t in x:
        if t == "(":
            count += 1
        elif t == ")":
            count -= 1

        if count < 0:
            flag = False
            break

    if count > 0:
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")