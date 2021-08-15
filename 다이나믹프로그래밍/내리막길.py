# https://www.acmicpc.net/problem/1520
# 접근방법
# DFS와 BFS의 경우
# - 만약 DFS나 BFS를 통해 탐색을 할 경우 러프하게 시간복잡도를 고려했을 때 4의 250000제곱만큼 연산을 하기 때문에 실패할 가능성이 크다.
# - 더군다나 메모리 제한이 128mb이기 때문에 메모리 초과가능성도 높다.

# 0. 주어진 지도를 입력받고, 지도의 크기만큼 dp테이블을 0으로 초기화한다. 단, 시작위치인 0, 0은 1응 저장한다.
# 1. 가장 오른쪽 아래에서부터 탐색을 시작해 상하좌우의 지역 중 현재 위치보다 높은 곳을 탐색한다.
# 2. 상하좌우 중 현재 위치보다 높은 곳의 dp값이 있다면 해당 값을 모두 더한 값을 현재 위치에 저장한다.
# 3. 상하좌우 중 현재 위치보다 높은 곳의 dp값이 없다면 해당 위치에서 재탐색하며 위의 과정을 반복한다.
# 4. 모든 탐색이 끝난 뒤, 해당 값을 출력한다.
import sys
sys.setrecursionlimit(10**5)
m, n = map(int, sys.stdin.readline().split())
map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dp[0][0] = 1

def dfs(row, col):
    if dp[row][col] >= 0:
        return dp[row][col]

    count = 0
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0<=row+dr<=m-1 and 0<=col+dc<=n-1 and map_[row][col] < map_[row+dr][col+dc]:
            count += dfs(row+dr, col+dc)
    dp[row][col] = count
    return dp[row][col]
    
dfs(m-1, n-1)
print(dp[m-1][n-1])