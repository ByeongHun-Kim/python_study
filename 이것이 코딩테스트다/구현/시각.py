import sys

N = int(sys.stdin.readline())

result = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            time = f"{h}{m}{s}"
            if '3' in time:
                result += 1

print(result)
