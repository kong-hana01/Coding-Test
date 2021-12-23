# https://www.acmicpc.net/problem/11378
# 접근 방법
# 처음 모든 사람에 대해 이분매칭을 동작한 뒤, 한번 더 모든 사람에 대해 이분 매칭을 반복한다. 단, 한 사람에 대해서 while 반복문을 활용해 dfs가 true일 경우 이를 반복해주며, k를 줄여나가고 만약 k가 0이라면 이분 매칭을 멈추고 결과를 출력한다.
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
input = sys.stdin.readline
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
    while True:
        visited = [False for _ in range(n+1)]
        if not dfs(i) or k == 0:
            break
        count += 1
        k -= 1
        
    if k == 0:
        break
print(count)