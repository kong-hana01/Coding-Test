# https://www.acmicpc.net/problem/2357
# 접근 방법
# 세그먼트 트리를 사용해 최소값과 최대값을 가진 배열을 두어 이를 활용해 계산한다.
def init(start, end, node):
    if start == end:
        tree[node] = [nodes[start], nodes[start]]
        return tree[node]
    mid = (start + end) // 2
    n1 = init(start, mid, node*2)
    n2 = init(mid+1, end, node*2+1)
    tree[node] = [min(n1[0], n2[0]), max(n1[1], n2[1])]
    return tree[node]

def query(left, right, node, start, end):
    if end < left or start > right:
        return []
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    n1 = query(left, right, node*2, start, mid)
    n2 = query(left, right, node*2+1, mid+1, end)
    if n1 and n2:
        return [min(n1[0], n2[0]), max(n1[1], n2[1])]
    elif n1:
        return n1
    return n2

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nodes = [int(input()) for _ in range(n)]
tree = [0 for _ in range(n*4)]
init(0, n-1, 1)
for _ in range(m):
    a, b = map(int, input().split())
    print(*query(a-1, b-1, 1, 0, n-1))
