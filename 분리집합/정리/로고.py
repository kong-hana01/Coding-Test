# https://www.acmicpc.net/problem/3108
# 접근 방법
# 이중 반복문을 통해 서로 다른 두 개의 직사각형을 탐색하며 유니온 파인드를 진행한다.
# 모든 반복문을 끝낸 뒤, 0, 0을 지나는 선분이 있는 지 확인하고, 있다면 집합의 개수를, 없다면 집합의 개수 + 1을 출력한다.
def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_find(x1, x2):
    x1_parent = get_parent(x1)
    x2_parent = get_parent(x2)
    if x1_parent < x2_parent:
        parent[x2_parent] = x1_parent
    else:
        parent[x1_parent] = x2_parent

def intersect_check(i, j):
    x01, y01, x02, y02 = square[i]
    x11, y11, x12, y12 = square[j]
    if x12 < x01 or x11 > x02 or y11 > y02 or y12 < y01 or (x01 < x11 < x12 < x02 and y01 < y11 < y12 < y02) or (x11 < x01 < x02 < x12 and y11 < y01 < y02 < y12):
        return False
    return True

n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
start_point = [0, 0]
for i in range(n):
    for j in range(i+1, n):
        if intersect_check(i, j):
            union_find(i, j)

union_set = set()
intersect_point = 0
count = 0
for i in range(n):
    x1, y1, x2, y2 = square[i]
    if not intersect_point and ((x1 <= start_point[0] <= x2 and start_point[1] in [y1, y2]) or (y1 <= start_point[1] <= y2 and start_point[0] in [x1, x2])):
        intersect_point = 1
    idx = get_parent(i)
    if idx not in union_set:
        union_set.add(idx)
        count += 1
print(count - intersect_point)