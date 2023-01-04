A = list(map(int, input().split()))

result = min(A)
while True:
    count = 0
    result += 1
    for i in A:
        if result % i == 0:
            count += 1
    if count >= 3:
        break
print(result)