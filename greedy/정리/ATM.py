n = int(input())
line = list(map(int, input().split()))
print(sum([x *(n-i) for i, x in enumerate(sorted(line))]))