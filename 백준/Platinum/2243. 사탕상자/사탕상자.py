# https://www.acmicpc.net/problem/2243
# 접근 방법
# 세그먼트 트리를 통해 구간 합을 구한 뒤, 각 구간에 따라 어느 상자에서 사탕을 뺄지 정한다.
def query(left, right, node, start, end):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2

    return query(left, right, node * 2, start, mid) + query(left, right, node * 2 + 1, mid + 1, end)

def update(x, y, node, start, end):
    if start == end:
        last_value = tree[node]
        tree[node] += y
        return tree[node] - last_value

    mid = (start + end) // 2
    last_value = tree[node]
    if x > mid:
        tree[node] += update(x, y, node * 2 + 1, mid + 1, end)
    else:
        tree[node] += update(x, y, node * 2, start, mid)
    return tree[node] - last_value

def pick_candy(target, node, start, end):
    if start == end:
        update(start, -1, 1, 0, m-1)
        return start
    mid = (start + end) // 2
    cnt = tree[node*2]
    if cnt >= target:
        return pick_candy(target, node * 2, start, mid)
    return pick_candy(target-cnt, node * 2 + 1, mid + 1, end)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
m = 1000001
tree = [0 for _ in range(m * 3)]
for _ in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        print(pick_candy(arr[1], 1, 0, m-1))
    else:
        update(arr[1], arr[2], 1, 0, m-1)
