# https://www.acmicpc.net/problem/17352
# 접근방법
# 분리집합을 통해 각 집합을 갱신하고, 집합에 포함되지 않는 섬과 집합에 포함되는 섬을 하나씩 출력한다.
def get_parent(idx):
    if island[idx] == idx:
        return idx
    index = get_parent(island[idx])
    island[idx] = index
    return index

def find_union(i1, i2):
    x1 = get_parent(i1)
    x2 = get_parent(i2)
    if x1 < x2:
        island[x2] = x1
    else:
        island[x1] = x2


import sys
input = sys.stdin.readline

n = int(input())
island = [i for i in range(n+1)]
for _ in range(n-2):
    i1, i2 = map(int, input().split())
    find_union(i1, i2)

for i in range(1, n+1):
    if i == island[i]:
        island1 = i
for i in range(1, n+1):
    if i != island1:
        island2 = i
        break
print(island1, island2)