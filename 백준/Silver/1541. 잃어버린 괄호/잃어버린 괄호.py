import sys
N = list(sys.stdin.readline().split("-"))

if len(N) == 1:
    print(eval(N[0]))
    exit(0)

data = []
for i in range(len(N)):
    data.append(list(map(lambda x: int(x.lstrip("0").strip()), N[i].split("+"))))

result = sum(data[0])
for i in data[1:]:
    result -= sum(i)
print(result)