# 접근 방법
# dfs탐색을 통해 각 건물을 짓기위해 필요한 건물을 짓는데 소요되는 시간을 저장하여 그 중 최댓값을 골라 본인의 건물을 짓는데 소요되는 시간을 저장한다.
import sys
input = sys.stdin.readline
n = int(input())
building = [[]]
time = [0]
dp = [0 for _ in range(n+1)]
for i in range(n):
    temp = list(map(int, input().split()))
    time.append(temp[0])
    building.append(temp[1:-1])

def dfs(x):
    if dp[x]:
        return dp[x]
    
    max_time = 0
    for x_ in building[x]:
        t = dfs(x_)
        max_time = max(t, max_time)
        
    dp[x] = max_time + time[x]
    return dp[x]

for x in range(1, n+1):
    if not dp[x]:
        dfs(x)
    print(dp[x])