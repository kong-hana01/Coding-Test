# https://www.acmicpc.net/problem/24391
# 접근 방법
# 분리집합을 통해 건물의 집합을 구한 뒤, 시간표 순서별로 집합이 다를 때 체크해 출력한다.
def get_parent(node):
    if node == parent[node]:
        return node
    parent[node] = get_parent(parent[node])
    return parent[node]

def find_union(node1, node2):
    parent1, parent2 = get_parent(node1), get_parent(node2)
    parent[parent1] = parent2

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    find_union(i, j)
schedule = list(map(int, input().split()))
result = 0
for i in range(1, n):
    if get_parent(schedule[i]) != get_parent(schedule[i-1]):
        result += 1
print(result)