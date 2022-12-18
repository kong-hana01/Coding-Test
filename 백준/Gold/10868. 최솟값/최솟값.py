# https://www.acmicpc.net/problem/10868
# 접근 방법
# 세그먼트 트리를 활용해 문제를 해결한다.
def init_tree(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    min_value = min(init_tree(start, mid, node * 2), init_tree(mid+1, end, node*2+1))
    tree[node] = min_value
    return tree[node]

def find_min_value(left, right, start, end, node):
    if right < start or left > end:
        return 1000000001
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    min_value = min(find_min_value(left, right, start, mid, node*2), find_min_value(left, right, mid+1, end, node*2+1))
    return min_value

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]
tree = [1000000001 for _ in range(n*4)]
init_tree(1, n, 1)
for _ in range(m):
    a, b = map(int, input().split())
    print(find_min_value(a, b, 1, n, 1))