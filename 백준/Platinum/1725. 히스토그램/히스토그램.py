# https://www.acmicpc.net/problem/1725
# 접근 방법
# 세그먼트 트리를 만들어서 이를 구현한다.
def init(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    mid = (start + end) // 2
    left = init(node*2, start, mid)
    right = init(node*2+1, mid+1, end)
    if arr[left] < arr[right]:
        tree[node] = left
    else:
        tree[node] = right
    return tree[node]

def query(node, left, right, start, end):
    if right < start or end < left:
        return -1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    n1 = query(node*2, left, right, start, mid)
    n2 = query(node*2+1, left, right, mid+1, end)
    if n1 == -1:
        return n2
    if n2 == -1:
        return n1
    if arr[n1] < arr[n2]:
        return n1
    return n2

def find_max_width(left, right):
    global result
    if left > right:
        return 
    if left == right:
        result = max(result, arr[left])
        return 
    min_height_idx = query(1, left, right, 0, n-1)
    result = max(result, (arr[min_height_idx] * (right - left + 1)))
    find_max_width(left, min_height_idx-1)
    return find_max_width(min_height_idx+1, right)

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
tree = [-1 for _ in range(n*4)]
result = 0
init(1, 0, n-1)
find_max_width(0, n-1)
print(result)