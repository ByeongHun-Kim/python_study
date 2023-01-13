import sys
N = int(sys.stdin.readline().strip())

numbers = []
for i in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        numbers = numbers[:len(numbers)-1]
    else:
        numbers.append(number)

print(sum(numbers))