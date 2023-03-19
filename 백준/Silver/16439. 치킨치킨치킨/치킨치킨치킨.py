# https://www.acmicpc.net/problem/16439
from itertools import combinations
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i, j, k in combinations(range(m), 3):
    sat = 0
    for x in arr:
        sat += max(x[i], x[j], x[k])
    result = max(result, sat)
print(result)