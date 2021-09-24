# https://www.acmicpc.net/problem/4803
# 접근 방법
# 분리 집합을 사용해 총 집합의 개수를 센다.
def get_parent(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = get_parent(parent[idx])
    return parent[idx]

def find_union(x1, x2):
    idx1 = get_parent(x1)
    idx2 = get_parent(x2)
    if idx1 > idx2:
        parent[idx1] = idx2
    elif idx1 < idx2:
        parent[idx2] = idx1
    else:
        parent[idx1] = 0
        parent[idx2] = 0
import sys
input = sys.stdin.readline
num = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    parent = [i for i in range(n+1)]

    for _ in range(m):
        x1, x2 = map(int, input().split())
        find_union(x1, x2)
        
    count = set()
    for i in range(1, n+1):
        p = get_parent(parent[i])
        if p and p not in count:
            count.add(parent[i])

    case = f'Case {num}'
    if len(count) == 0:
        print(f'{case}: No trees.')
    elif len(count) == 1:
        print(f'{case}: There is one tree.')
    else:
        print(f'{case}: A forest of {len(count)} trees.')
    num += 1