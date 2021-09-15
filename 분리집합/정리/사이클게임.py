# https://www.acmicpc.net/problem/20040
# 접근 방법
# 분리집합을 통해 부분집합들을 갱신해나가다가 유니온 파인드를 했을 때 같은 숫자가 나온 경우 몇번째 차례였는지 출력한다.
def get_parent(idx):
    if parent[idx] == idx:
        return idx
    index = get_parent(parent[idx])
    parent[idx] = index
    return index

def find_union(point1, point2):
    p1 = get_parent(point1)
    p2 = get_parent(point2)
    if p1 == p2:
        return True
    
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2
    return False

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
array = [list(map(int, input().split())) for _ in range(m)]
for i in range(1, m+1):
    point1, point2 = array[i-1]
    check = find_union(point1, point2)
    if check:
        break
    
if check:
    print(i)
else:
    print(0)