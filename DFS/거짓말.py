# https://www.acmicpc.net/problem/1043
# 접근 방법
# 파티에 오는 사람의 번호를 인덱스로 하고, 그 사람과 같은 파티에 참석하는 사람을 리스트로 가지는 그래프를 초기화한다.
# 진실을 아는 사람들을 인덱스로 하는 그래프를 탐색하며 방문처리를 한다.
# 이후 party를 하나씩 탐색하며 진실을 아는 사람이 없는 파티의 수를 센 뒤, 이를 출력한다.
n, m = map(int, input().split())
array = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def dfs(x):
    visited[x] = True

    for x_ in graph[x]:
        if not visited[x_]:
            dfs(x_)

# 그래프 초기화
for data in party:
    for i in range(data[0]):
        for j in range(i+1, data[0]):
            graph[data[i+1]].append(data[j+1])
            graph[data[j+1]].append(data[i+1])

# 진실을 알게 되는 사람의 명단 초기화
for i in range(array[0]):
    x = array[i+1]
    dfs(x)

# 파티에 참석한 사람 확인
result = 0
for i in range(m):
    count = 0
    for x in party[i][1:]:
        if not visited[x]:
            count += 1
    
    if party[i][0] == count:
        result += 1

print(result)