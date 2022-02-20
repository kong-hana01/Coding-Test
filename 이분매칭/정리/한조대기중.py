# https://www.acmicpc.net/problem/14433
# 접근 방법
# 각 팀에 대해 이분매칭을 구현한 뒤 개수를 비교해 결과를 출력한다.
def dfs(x):
    if visited[x]:
        return False
    visited[x] = True
    for i in team[x]:
        if not champ[i] or dfs(champ[i]):
            champ[i] = x
            return True
    return False


n, m, k1, k2 = map(int, input().split())
result = []
for k in [k1, k2]:
    champ = [[] for _ in range(m+1)]
    team = [[] for _ in range(n+1)]
    count = 0
    for _ in range(k):
        i, j = map(int, input().split())
        team[i].append(j)
    for i in range(1, n+1):
        visited = [False for _ in range(n+1)]
        if dfs(i):
            count += 1
    result.append(count)
    
if result[0] < result[1]:
    print('네 다음 힐딱이')
else:
    print('그만 알아보자')