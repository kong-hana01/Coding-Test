# https://www.acmicpc.net/problem/6549
# 접근 방법
# 세그먼트 트리를 사용해 구간에서 가장 높은 높이를 저장하여 dfs를 사용해 가장 넓은 직사각형을 찾는다.
def init(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node] # tree[node]에는 해당 범위에서 가장 작은 값을 가진 인덱스가 포함
    
    mid = (start + end) // 2
    n1 = init(node * 2, start, mid)
    n2 = init(node * 2 + 1, mid + 1, end)
    if arr[n1] >= arr[n2]:
        tree[node] = n2
    else:
        tree[node] = n1
    return tree[node]

def query(left, right, node, start, end):
    global result
    if end < left or start > right:
        return -1
    elif left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    n1 = query(left, right, node * 2, start, mid)
    n2 = query(left, right, node * 2 + 1, mid + 1, end)
    if n1 != -1 and n2 != -1:
        if arr[n1] >= arr[n2]:
            return n2
        return n1
    elif n1 != -1:
        return n1
    else:
        return n2

def get_max_width(left, right):
    if left > right:
        return 0
    global result
    if left == right:
        result = max(result, arr[left])
        return arr[left]
    min_height_idx = query(left, right, 1, 0, n-1)
    result = max(result, (right-left+1) * arr[min_height_idx])
    get_max_width(left, min_height_idx-1)
    get_max_width(min_height_idx+1, right)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
while True:
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    if n == 0:
        break
    tree = [0 for _ in range(n *4)]
    result = 0
    init(1, 0, n-1)
    get_max_width(0, n-1)
    print(result)