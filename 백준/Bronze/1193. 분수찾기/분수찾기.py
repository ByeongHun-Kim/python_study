N = int(input())
count, n = 0, 1
while 1:
    before = count
    count += n
    if count >= N:
        break
    n += 1

if n % 2 == 0:
    print(f"{N - before}/{n+1-N+before}")
else:
    print(f"{n + 1 - N + before}/{N - before}")