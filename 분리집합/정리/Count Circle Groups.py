# https://www.acmicpc.net/problem/10216
# 접근 방법
# 적군의 진영을 이중 반복문을 통해 서로 같은 그룹인지 확인한다.
# 같은 그룹임을 확인하면 낮은 인덱스 번호로 초기화하는 유니온 파인드를 활용한다.
def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


def find_group(x1, x2):
    parent1 = get_parent(x1)
    parent2 = get_parent(x2)
    if parent1 > parent2:
        parent[parent1] = parent2
    else:
        parent[parent2] = parent1



import sys, math
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    parent = [i for i in range(n)]
    for i in range(n):
        x1, y1, r1 = array[i]
        for j in range(i+1, n):
            x2, y2, r2 = array[j]
            if math.sqrt((x1-x2)**2 + (y1-y2)**2) <= r1+r2:
                find_group(i, j)
    count_group = set()
    for i in range(n):
        x = get_parent(i)
        if x not in count_group:
            count_group.add(x)

    print(len(count_group))