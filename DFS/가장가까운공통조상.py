# https://www.acmicpc.net/problem/3584
# 접근 방법
# 리스트로 트리를 구현한 뒤, DFS를 활용해 두 노드의 부모노드를 차례로 저장한뒤, 가장 가까운 공통 조상을 출력한다.
def dfs(x, nodes):
    nodes.append(x)
    if not tree[x]:
        return 
    dfs(tree[x], nodes)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
tc = int(input())
for _ in range(tc):
    n = int(input())
    tree = [0 for _ in range(n + 1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[b] = a
    a, b = map(int, input().split())
    parentA, parentB = [], []
    dfs(a, parentA)
    dfs(b, parentB)
    parentA = set(parentA)

    for x in parentB:
        if x in parentA:
            print(x)
            break
    