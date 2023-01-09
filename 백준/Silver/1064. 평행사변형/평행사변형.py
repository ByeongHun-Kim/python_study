import sys

xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().split())

# AB == AC
if (xa - xb) * (yb - yc) == (xb - xc) * (ya - yb):
    print(-1.0)
    exit(0)

ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
ac = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
bc = ((xc - xb) ** 2 + (yc - yb) ** 2) ** 0.5

length_list = [ab + ac, ab + bc, ac + bc]
result = max(length_list) - min(length_list)
print(2 * result)
