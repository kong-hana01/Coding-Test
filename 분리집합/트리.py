# https://www.acmicpc.net/problem/13306
# 접근 방법
# 0. 딕셔너리르 통해 부모가 value이고 자식이 key인 트리를 구현한다.
# 1. 각 집합을 나타낼 parent는 1로 초기화 한 뒤, 트리의 에지를 제거할 때마다 자기 자신의 인덱스를 값으로 갱신해준다.
# 2. 분리집합을 통해 각 트리의 집합을 매번 갱신한 뒤, 집합이 같으면 YES, 다르면 NO를 출력한다.
def get_parent(x):
    if x == parent[x]:
        return x
    parent[x] = get_parent(tree[x])
    return parent[x]

import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline
n, q = map(int, input().split())
tree = [1 for _ in range(n+1)]
for i in range(2, n+1):
    tree[i] = int(input())
parent = [1 for _ in range(n+1)]
for _ in range(q + n - 1):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        b = temp[1]
        parent[b] = b
    else:
        c, d = temp[1], temp[2]
        if get_parent(c) == get_parent(d):
            print('YES')
        else:
            print('NO')