# https://www.acmicpc.net/problem/17250
# 접근 방법
# 분리 집합을 사용해 문제를 해결한다.
# 이때 각 집합마다 행성에 대한 정보를 가지고 있어 집합을 합칠 때 이를 출력한다.
def get_parent(node):
    if node == parent[node]:
        return node
    parent[node] = get_parent(parent[node])
    return parent[node]

def find_union(n1, n2):
    p1 = get_parent(n1)
    p2 = get_parent(n2)
    if p1 == p2:
        return max(galaxy[p1], galaxy[p2])
    parent[p2] = p1
    galaxy[p1] += galaxy[p2]
    galaxy[p2] = 0
    return galaxy[p1]
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
galaxy = [int(input()) for _ in range(n)]
parent = [i for i in range(n)]
for _ in range(m):
    x, y = map(lambda x: x-1, map(int, input().split()))
    print(find_union(x, y))