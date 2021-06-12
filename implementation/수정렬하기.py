import sys
n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)].sort()
for x in array:
    print(x)