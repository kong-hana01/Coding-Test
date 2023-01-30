# https://www.acmicpc.net/problem/16988
# 접근 방법
# 2번 돌과 인접한 0인 지역을 따로 저장한 뒤, 이 위치에 바둑을 두어 최대 몇 개의 바둑을 제거할 수 있는 지 센다.
def bfs(r, c):
    queue = deque([])
    queue.append([r, c])
    union.append(1)
    union_num = len(union) - 1
    near[union_num] = []
    visited[r][c] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if not (0<=r+dr<n and 0<=c+dc<m):
                continue
            if graph[r+dr][c+dc] == 2 and not visited[r+dr][c+dc]:
                queue.append([r+dr, c+dc])
                union[union_num] += 1
            elif graph[r+dr][c+dc] == 0 and [r+dr, c+dc] not in near[union_num]:
                near[union_num].append([r+dr, c+dc])
                if not visited[r+dr][c+dc]:
                    total_near.append([r+dr, c+dc])
            visited[r+dr][c+dc] = True

def find_max_count_of_delete(start, check_set):
    global result
    if len(check_set) == 2:
        result = max(result, find_count_of_delete(check_set))
        return
    elif len(check_set) == 1:
        result = max(result, find_count_of_delete(check_set))
        
    for i in range(start, len(total_near)):
        if i in check_set:
            continue
        find_max_count_of_delete(i+1, check_set | {i})

def find_count_of_delete(check_set):
    cnt = 0
    place = []
    for i in check_set:
        place.append(total_near[i])
    for key, values in near.items():
        is_in = True
        for value in values:
            if value not in place:
                is_in = False
                break
        if is_in:
            cnt += union[key]
    return cnt

from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
total_near = []
near = {}
union = []
visited = [[False for _ in range(m)] for _ in range(n)]
for r in range(n):
    for c in range(m):
        if graph[r][c] == 2 and not visited[r][c]:
            bfs(r, c)
result = 0
find_max_count_of_delete(0, set([]))
print(result)