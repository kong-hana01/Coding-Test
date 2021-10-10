# 접근 방법
# 딕셔너리를 통해 트리를 구현하고 이를 bfs로 하나씩 탐색하며 최소 시간을 출력한다.
# 단 최소 시간을 출력하기 위해서 각 노드를 dfs로 탐색하며 하위 부분 트리의 노드가 얼마나 있는 지를 저장한 뒤, 가장 많은 순서부터 bfs를 탐색한다.
def dfs(i):
    if dp[i] or not emp[i]:
        return dp[i]
    temp = []
    for x in emp[i]:
        count = dfs(x) + 1
        temp.append(count)
    temp.sort(reverse = True)
    max_count = temp[0]
    now_time = max_count
    count = 0
    for m in temp[1:]:
        now_time -= 1
        if now_time < m:
            count += 1

    dp[i] = max_count + count
    return dp[i]
        

from collections import deque
n = int(input())
emp = {}
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
for i in range(n):
    emp[i] = []
    
for i in range(1, n):
    x = arr[i]
    emp[x].append(i)
print(emp)
# for k in emp.keys():
#     if not emp[k]:
#         dp[k] = 1
dfs(0)
print(dp[0])
# print(dp)      
