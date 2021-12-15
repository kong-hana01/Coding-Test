# https://www.acmicpc.net/problem/11377
# 접근 방법
# 처음 모든 사람에 대해 이분 매칭을 진행한 뒤, 다시 한번 모든 인원에 대해 이분 매칭을 진행한다. 이때 이분매칭으로 일이 매칭된 사람들은 최대 k명까지만 되야하므로 k명이 넘게되면 이를 중단하고 값을 출력한다.
def dfs(i):
    if visited[i]:
        return False
    visited[i] = True
    for x in emp[i]:
        if not work[x] or dfs(work[x]):
            work[x] = i
            return True
    return False


import sys
n, m, k = map(int, input().split())
emp = [[] for _ in range(n+1)]
work = [0 for _ in range(m+1)]
for i in range(1, n+1):
    temp = list(map(int, input().split()))
    emp[i] = temp[1:]

count = 0
for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    if dfs(i):
        count += 1

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    if dfs(i):
        count += 1
        k -= 1
        if k == 0:
            break
print(count)
