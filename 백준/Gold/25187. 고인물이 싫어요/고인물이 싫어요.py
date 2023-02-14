# https://www.acmicpc.net/problem/25187
# 접근 방법
# 분리집합을 사용해 문제를 해결한다.
def get_union(node):
    if union[node] == node:
        return node
    union[node] = get_union(union[node])
    return union[node]

def find_union(n1, n2):
    n1 = get_union(n1)
    n2 = get_union(n2)
    union[n2] = n1

import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
arr = list(map(int, input().split()))
union = [i for i in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    find_union(u, v)

count = {}
for i in range(1, n+1):
    union[i] = get_union(union[i])
    if union[i] not in count:
        count[union[i]] = [0, 0]
    count[union[i]][arr[i-1]] += 1

for _ in range(q):
    k = int(input())
    dirty_water, clean_water = count[union[k]]
    if clean_water > dirty_water:
        print(1)
    else:
        print(0)