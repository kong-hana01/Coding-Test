# 접근 방법
# 1. 주어진 칸만큼 dp테이블을 1로 초기화한다.
# 2. 이후 주어진 칸을 하나씩 탐색하며 현재 위치의 상하좌우에 현재 위치보다 많은 대나무가 있는 곳으로 이동해가며 방문처리하지 않는 BFS를 동작시킨다.(이동조건을 현재위치보다 많은 대나무가 있는 곳으로 이동하는 것으로만 제한한다. 어차피 중복되는 값을 계속 탐색해 recursion error에 빠지지 않기때문이다.)
# 2-1. 이때 dp테이블에 이동한 횟수 중 최댓값을 저장한다.
# 3. dp테이블에 2이상의 값이 있다면 이는 이미 탐색을 진행했던 칸이므로 해당 칸을 탐색하지 않고 다른 칸을 탐색한다.
# 4. 위의 과정을 모든 칸에 대해 반복한다.
import sys
sys.setrecursionlimit(10**6)

n = int(input())
map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


dp = [[0 for _ in range(n)] for _ in range(n)]

def dfs(row, col):

    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=row+dr<=n-1 and 0<=col+dc<=n-1 and map_[row+dr][col+dc] < map_[row][col]:
            if dp[row+dr][col+dc] <= dp[row][col]:
                dp[row+dr][col+dc] = dp[row][col] + 1
                dfs(row+dr, col+dc)
            
for row in range(n):
    for col in range(n):
        if dp[row][col] == 0:
            dfs(row, col)
            print(dp)

result = 0
for row in range(n):
    for col in range(n):
        result = max(dp[row][col], result)
print(result+1)