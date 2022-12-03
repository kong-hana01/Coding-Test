# https://www.acmicpc.net/problem/1275
# 접근 방법
# 세그먼트 트리로 값을 갱신하여 구간합을 구한다.
def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

def update(x, y, node, start, end):
    if start == end:
        last_value = tree[node]
        tree[node] = y
        return tree[node] - last_value
    mid = (start + end) // 2
    last_value = tree[node]
    if x <= mid:
        tree[node] += update(x, y, node*2, start, mid)
    else:
        tree[node] += update(x, y, node*2+1, mid+1, end)
    return tree[node] - last_value

def query(left, right, node, start, end):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(left, right, node * 2, start, mid) + query(left, right, node * 2 + 1, mid + 1, end)

import sys
input = sys.stdin.readline
n, q = map(int, input().split())
arr = list(map(int, input().split()))
tree = [0 for _ in range(n*4)]
init(1, 0, n-1)
for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(query(x-1, y-1, 1, 0, n-1))
    update(a-1, b, 1, 0, n-1)