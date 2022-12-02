# https://www.acmicpc.net/problem/2104
# 접근 방법
# 세그먼트 트리를 통해 구간에 대한 합과 최소값을 구한다.
def init(node, start, end):
    if start == end:
        tree[node] = [arr[start], start] # 합, 최소값을 의미하는 인덱스
        return tree[node]
    mid = (start + end) // 2
    n1 = init(node*2, start, mid)
    n2 = init(node*2+1, mid+1, end)
    if arr[n1[1]] < arr[n2[1]]:
        min_idx = n1[1]
    else:
        min_idx = n2[1]
    tree[node] = [n1[0]+n2[0], min_idx]
    return tree[node]

def query(left, right, node, start, end):
    if left > end or right < start:
        return []
    elif left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    n1 = query(left, right, node*2, start, mid) 
    n2 = query(left, right, node*2 + 1, mid + 1, end) 
    if n1 and n2:
        if arr[n1[1]] < arr[n2[1]]:
            min_idx = n1[1]
        else:
            min_idx = n2[1]
        return [n1[0]+n2[0], min_idx]
    elif n1:
        return n1
    else:
        return n2 
    
def get_max_score(left, right):
    if left > right:
        return
    global result
    max_node = query(left, right, 1, 0, n-1)
    score = max_node[0] * arr[max_node[1]]
    result = max(result, score)
    get_max_score(left, max_node[1]-1)
    get_max_score(max_node[1]+1, right)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
arr = list(map(int, input().split()))
INF = 1000000
tree = [[] for _ in range(n*4)]
result = 0
init(1, 0, n-1)
get_max_score(0, n-1)
print(result)