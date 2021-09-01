# https://www.acmicpc.net/problem/10775
# 접근 방법
# 분리집합을 활용해 문제를 해결한다.
# 게이트만큼의 리스트를 해당 리스트의 번호로 값을 초기화한다.
# 비행기에 대한 정보를 하나씩 탐색하며 게이트에 비행기가 도착하게 될 경우 해당 게이트의 번호와 값이 같다면 해당 게이트에서 본인보다 낮은 곳의 인덱스를 가리키게 한다.
# 게이트의 번호가 다르다면 부모 인덱스로 이동한 뒤, 해당 리스트의 값은 그 이전 인덱스를 가리킨다.
# 만약 이전 인덱스가 0이 나올 경우 탐색을 멈추고 비행기의 도킹 횟수를 출력한다.
def get_parent(a):
    if gate[a] == a:
        return a
    parent = get_parent(gate[a])
    gate[a] = parent
    return parent

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

g = int(input())
p = int(input())
gate = [i for i in range(g+1)]
plane = [int(input()) for _ in range(p)]
count = 0
for x in plane:
    value = get_parent(x)
    if value == 0:
        break
    count += 1
    gate[value] = value - 1
print(count)