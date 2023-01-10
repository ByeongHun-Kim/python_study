import sys
N = sys.stdin.readline().strip()

alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for alphabet in alphabets:
    N = N.replace(alphabet, '0')

print(len(N))