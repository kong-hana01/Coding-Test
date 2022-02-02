# https://www.acmicpc.net/problem/7511
# 접근 방법
# 분리집합을 통해 연결되어있는 집합의 인덱스 번호를 갱신해가며 테스트 케이스별로 출력조건에 맞게 출력한다.
def get_parent(friend):
    if parent[friend] == friend:
        return friend
    parent[friend] = get_parent(parent[friend]) 
    return parent[friend]

def find_union(friend1, friend2):
    n1 = get_parent(friend1)
    n2 = get_parent(friend2)
    if n1 > n2:
        parent[n1] = n2
    else:
        parent[n2] = n1
    
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
tc = int(input())
for i in range(1, tc+1):
    n, k = int(input()), int(input())
    parent = [j for j in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        find_union(a, b)
    print(f'Scenario {i}:')
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        if get_parent(u) == get_parent(v):
            print(1)
        else:
            print(0)
    print()