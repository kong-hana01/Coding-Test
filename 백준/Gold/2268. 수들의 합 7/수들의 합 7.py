# https://www.acmicpc.net/problem/2268
# 접근 방법
# 세그먼트 트리를 사용한다.
def query(node, start, end, left, right):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_node = query(node*2, start, mid, left, right)
    right_node = query(node*2+1, mid+1, end, left, right)
    return left_node + right_node

def update(node, start, end, idx, value):
    if start == end:
        last = tree[node]
        tree[node] = value
        return value - last
    mid = (start + end) // 2
    if mid < idx:
        diff = update(node*2+1, mid+1, end, idx, value)
    else:
        diff = update(node*2, start, mid, idx, value)
    tree[node] += diff
    return diff



import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0 for _ in range(n)]
tree = [0 for _ in range(n*4)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        if b > c:
            b, c = c, b
        print(query(1, 0, n-1, b-1, c-1))
    else:
        update(1, 0, n-1, b-1, c)
