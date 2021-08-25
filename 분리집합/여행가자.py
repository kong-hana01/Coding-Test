# https://www.acmicpc.net/problem/1976
# 접근 방법 1
# 유니온 파인드를 활용해 연결된 집합을 확인한다.
def get_parent(index):
    if parent[index] == index:
        return index
    parent[index] = get_parent(parent[index])
    return parent[index]

def union_parent(a, b):
    x = get_parent(a)
    y = get_parent(b)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

def find_parent():
    standard = get_parent(plan[0])
    for x in plan[1:]:
        i = get_parent(x)
        if i != standard:
            print('NO')
            return
    print('YES')
    return 

# n = int(input())
# m = int(input())
# array = [list(map(int, input().split())) for _ in range(n)]
# plan = list(map(int, input().split()))
# parent = [i for i in range(n+1)]

# for i in range(1, n+1):
#     for j in range(i+1, n+1):
#         if array[i-1][j-1] == 1:
#             union_parent(i, j)
# find_parent()


# 접근 방법 2
# 일반적인 구현을 통해 한 도시에서 탐색 중인 다른 도시 중 1로 연결된 게 하나도 없을 경우 NO를 리턴하고 모든 도시가 최소한 연결 된 도시가 한 개 이상이라면 YES를 리턴한다.
# 연결된 도시의 집합이 하나가 아닐 경우 해당 접근 방법은 틀릴 수 있다.
# n = int(input())
# m = int(input())
# array = [list(map(int, input().split())) for _ in range(n)]
# plan = list(map(int, input().split()))
# parent = [0 for i in range(n+1)]

# def visit_city():
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if array[i-1][j-1]:
#                 parent[i] = 1
#                 parent[j] = 1

#     for x in plan:
#         if parent[x] == 0:
#             print('NO')
#             return
#     print('YES')
#     return

# visit_city()

# 접근 방법 3
# 그래프 자료구조를 활용해 dfs로 연결된 도시의 집합을 찾는다.
n = int(input())
m = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
union = [0 for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if array[i][j]:
            graph[i+1].append(j+1)
def dfs(x, num):
    union[x] = num
    for x_ in graph[x]:
        if not union[x_]:
            dfs(x_, num)
num = 1
for x in plan:
    if not union[x]:
        dfs(x, num)
        num += 1

def visit_city2():
    s = union[plan[0]]
    for x in plan:
        if s != union[x]:
            print('NO')
            return
    print('YES')
    return

visit_city2()