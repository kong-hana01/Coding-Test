# https://www.acmicpc.net/problem/2668
# 접근방법
# 리스트의 인덱스를 하나씩 탐색하며 그 인덱스의 값을 기준으로 dfs 탐색을 진행한다.
# 주의 사항
# - 리스트를 하나씩 탐색할 때마다 방문처리 리스트를 매번 초기화한다.
# - dfs를 통해 처음 위치로 다시 방문을 하게된다면 방문처리한 개수를 모두 저장한다.
# - 집합에 포함된 인덱스에 대해선 따로 방문처리를 진행하여 나중에 방문처리를 할 수 없도록 한다.
def dfs(s, x):
    visited[x] = True
    if visited_set[x]:
        return False
    if arr[x] == s:
        return True
    if visited[arr[x]]:
        return False

    if dfs(s, arr[x]):
        return True
    return False


n = int(input())
arr = [0] + list(int(input()) for _ in range(n))
visited_set = [False for _ in range(n+1)]
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    if dfs(i, i):
        for j in range(1, n+1):
            if visited[j]:
                visited_set[j] = True
print(sum([1 if x else 0 for x in visited_set ]))
for i in range(1, n+1):
    if visited_set[i]:
        print(i)