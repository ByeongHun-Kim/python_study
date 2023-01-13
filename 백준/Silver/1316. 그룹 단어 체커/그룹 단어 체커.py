import sys
N = int(sys.stdin.readline().strip())

words = []
for i in range(N):
    words.append(sys.stdin.readline())

count = 0
for word in words:
    before = ""
    token = []
    flag = True
    for w in word:
        if (before != w) & (w in token):
            flag = False
            break

        elif (before != w) & (w not in token):
            before = w
            token.append(w)
    if flag is True:
        count += 1

print(count)