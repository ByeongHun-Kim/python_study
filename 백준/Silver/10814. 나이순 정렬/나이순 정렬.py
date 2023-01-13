import sys
N = int(sys.stdin.readline().strip())

names = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    names.append((int(age), name))

names.sort(key=lambda x: x[0])

for n in names:
    print(n[0], n[1])