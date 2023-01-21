import sys

N = sys.stdin.readline().strip()

ones = N.split('0')
ones = list(filter(None, ones))

zeros = N.split('1')
zeros = list(filter(None, zeros))

if len(ones) == 0 or len(zeros) == 0:
    print(0)

else:
    print(min([len(ones), len(zeros)]))