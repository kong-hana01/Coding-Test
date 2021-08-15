# 접근방법 -> 위상 정렬 배운 뒤, 재시도
# 0. 주어진 k만큼 특정 건물을 지어야하는 순서를 입력받을 때 건물 번호를 인덱스로 하고, 그 건물을 짓기위해 선행해서 지어야하는 건물을 값으로 하는 그래프(building)로 저장하고 각 건물이 지어진 시간을 저장할 dp테이블을 초기화한다.
# 1. target이되는 building을 dps를 통해 해당 건물을 짓기 위해 먼저 지어야하는 건물들을 탐색한다.
# 1-1. 지어야하는 건물이 없는 경우 해당 건물 번호를 인덱스로 가지는 dp 테이블의 값에 해당 건물을 짓는데 소요되는 시간을 저장한다.
# 1-2. 지어야하는 건물이 하나만 있는 경우는 그 건물을 짓는데 소요되는 시간 + 해당 건물을 짓는데 소요되는 시간을 저장한다.
# 1-3.지어야하는 건물이 여러 개인 경우는 그 건물을 짓는데 소요되는 시간 중 가장 오래걸리는 시간 + 해당 건물을 짓는데 소요되는 시간을 저장한다.
# 1-4. 건물을 짓는데 들어가는 시간을 확인할 때는 dp테이블을 확인하고 값이 0인 경우에는 dfs 탐색하고, 값이 있는 경우는 해당 값을 리턴한다.
# 2. 모든 탐색을 완료한 뒤, 가장 큰 값을 출력한다.

import sys
sys.setrecursionlimit(10**6)
def dfs(x):
    global result
    if dp[x]:
        return dp[x]
    
    time = 0
    for x_ in building[x]:
        time = max(time, dfs(x_))
    dp[x] = time + build_time[x]
    result = max(result, dp[x])
    return dp[x]

for tc in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    build_time = [0] + list(map(int, sys.stdin.readline().split()))
    building = [[] for _ in range(n+1)]
    dp = [0] * (n+1)
    result = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        building[y].append(x)
    target = int(sys.stdin.readline())
    dfs(target)
    print(result)