# https://www.acmicpc.net/problem/14595
# 접근 방법
# 분리집합을 사용해 문제를 해결한다.
def get_parent(node):
    if node == room[node]:
        return node
    room[node] = get_parent(room[node])
    return room[node]

def find_union(r1, r2):
    room[r1] = r2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
m = int(input())
room = [i for i in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    i = get_parent(x)
    while i <= y:
        r1 = get_parent(i)
        r2 = get_parent(y)
        find_union(r1, r2)
        if r1 == i:
            i += 1
        else:
            i = r1 + 1

check_set = set([])
for i in range(1, n+1):
    check_set.add(get_parent(i))
print(len(check_set))