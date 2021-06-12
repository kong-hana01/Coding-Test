# n = int(input())
# vertex = [list(map(int, input().split())) for _ in range(n)]
# hole = int(input())
# hole_vertex = sorted([list(map(int, input().split)) for _ in range(hole)], key = lambda x: x[1])

# 열 행 구조
n = 14
vertex = [[0, 0], [0, 5], [1, 5], [1, 3], [2, 3], [2, 4], [3, 4], [3, 2], [5, 2], [5, 4], [6, 4], [6, 3], [8, 3], [8, 0]]
hole = 2
hole_vertex = sorted([[1, 3, 2, 3], [3, 2, 5, 2]], key = lambda x: x[1])
visited = [False] * len(hole_vertex)


# 방법 1
# 1. 구멍이 높은 위치에 있는 것부터 차례로 왼쪽 오른쪽에 구멍이 있는 지 확인한다.
# 2. 구멍이 있다면 그 구멍을 다시 시작지점으로 지정해 왼쪽 오른쪽을 확인한다.
# 3. 구멍이 없다면 남아있는 물을 리턴한다.
# 보류

def check_water(v):
    visited[v] = True
    
    for i in range(len(hole_vertex)):
        if not visited[i] and i != v:
            check_water(i)

check_water(0)


