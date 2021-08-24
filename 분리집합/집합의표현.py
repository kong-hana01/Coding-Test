# 접근 방법
# 유니온 파인드를 사용해 같은 집합에 속하는지를 확인한다.
# 유니온 파인드
# 0. n+1개만큼 길이륵 가지는 리스트를 만들어 각각의 인덱스에 해당하는 값을 넣어 초기화한다.
# 1. 재귀함수를 활용해 부모노드를 구하는 함수를 만든다. 해당 함수는 인덱스와 값이 같은 경우에 최종적인 부모노드를 리턴하는 함수이다.
# 2. 합집합을 만드는 함수를 만든다. 해당 함수는 두 집합의 최종적인 부모노드의 값을 비교해 더 작은 값이 부모가 되도록(더 큰 값의 인덱스에 작은 값을 저장) 구현한다.
# 3. 같은 집합에 속해있는지 판단하는 함수를 만든다. 해당함수는 부모노드를 찾아 두 원소의 부모노드가 같다면 True, 아니면 False를 출력하도록한다.
def get_parent(index):
    if parent[index] == index:
        return index
    parent[index] = get_parent(parent[index])
    return parent[index]

def union_parent(a, b):
    x1 = get_parent(a)
    x2 = get_parent(b)
    parent[max(x1, x2)] = min(x1, x2)

def find_parent(a, b):
    x1 = get_parent(a)
    x2 = get_parent(b)
    if x1 != x2:
        return print('NO')
    else:
        return print('YES')

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    check, a, b = map(int, input().split())
    if check:
        find_parent(a, b)
    else:
        union_parent(a, b)