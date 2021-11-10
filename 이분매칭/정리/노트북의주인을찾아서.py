# https://www.acmicpc.net/problem/1298
# 접근방법
# 기본적인 이분매칭 알고리즘을 활용해 노트북이 매칭된 최대 개수를 출력한다.

def dfs(num):
    if visited[num]:
        return False
    visited[num] = True
    for x in graph[num]:
        if not laptop[x] or dfs(laptop[x]):
            laptop[x] = num
            return True
    return False


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
laptop = [0 for _ in range(n+1)]

count = 0
for num in range(1, n+1):
    visited = [False for _ in range(n+1)]
    if dfs(num):
        count += 1
print(count)