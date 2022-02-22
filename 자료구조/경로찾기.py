# https://www.acmicpc.net/problem/11403
# 접근 방법
# 주어진 그래프가 1인 경우 DFS를 통해 리스트에 들린 정점의 위치를 갱신해가며 반복문을 사용해 결과 그래프의 값을 1로 바꾼다.
def dfs(now):
    visited[now] = True
    for x in n_list:
        graph_[x][now] = 1
    for i in range(n):
        if not visited[i] and graph[now][i]:
            dfs(i)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
graph_ = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    n_list = []
    for j in range(n):
        if graph[i][j]:
            n_list.append(j)
    dfs(i)
print(graph_)