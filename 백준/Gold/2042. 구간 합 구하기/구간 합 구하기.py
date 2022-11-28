# https://www.acmicpc.net/problem/2042
# 접근 방법
# 값 변경이 빈번하게 일어나므로 세그먼트 트리를 사용해 문제를 해결한다.

# 점 갱신
def update(idx, value, node, start, end): 
    # idx번째 노드의 값을 value로 값을 바꾸는 경우, s와 e는 현재 인덱스의 범위
    if start == end:
        last_value = tree[node]
        tree[node] = value
        return value - last_value # 재귀적으로 갱신
    mid = (start+end) // 2
    if (idx > mid):
        diff = update(idx, value, node * 2 + 1, mid + 1, end)
    else:
        diff = update(idx, value, node * 2, start, mid)
    
    last_value = tree[node]
    tree[node] += diff
    return tree[node] - last_value

# 구간 합    
def query(left, right, node, start, end):
    # left, right는 구간합의 범위, start와 end는 현재 인덱스의 범위
    if end < left or start > right:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start + end) // 2
        return query(left, right, node * 2, start, mid) + query(left, right, node * 2 + 1, mid + 1, end)
    
def initTree(node, start, end):
    if start == end:
        tree[node] = leaf_nodes[start]
        return tree[node]

    mid = (start+end) // 2
    tree[node] = initTree(node*2, start, mid) + initTree(node*2+1, mid+1, end)
    return tree[node]

from math import sqrt
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
leaf_nodes = [int(input()) for _ in range(n)]
# n이 2의 배수 일 경우 리프노드의 개수 * 2 - 1이 노드의 총 개수
SIZE = n * 4
tree = [0 for _ in range(SIZE)]
initTree(1, 0, n-1)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b-1, c, 1, 0, n-1)
    else:
        print(query(b-1, c-1, 1, 0, n-1))
    
