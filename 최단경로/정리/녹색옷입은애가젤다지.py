# https://www.acmicpc.net/problem/4485
# 접근 방법
# 젤다의 시작 위치부터 우선순위 큐 + BFS를 활용해 가장 작은 비용이 드는 곳을 기준으로 이동한 뒤, (n-1, n-1)의 위치에 도달할 경우 결과를 출력한다.
import heapq, sys
input = sys.stdin.readline

def move(x, y, problem):
    dp[x][y] = cave[x][y]
    q = []
    heapq.heappush(q, (cave[x][y], x, y))
    
    while q:
        cost, r, c = heapq.heappop(q)
        if dp[r][c]<cost:
            continue
            
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<=n-1 and 0<=c+dc<=n-1 and dp[r+dr][c+dc] > cost + cave[r+dr][c+dc]:
                heapq.heappush(q, (cost+cave[r+dr][c+dc], r+dr, c+dc))
                dp[r+dr][c+dc] = cost+cave[r+dr][c+dc]
                
                if r+dr == n - 1 and c+dc == n - 1:
                    print('Problem {}: {}'.format(problem, dp[r+dr][c+dc]))
                    return

problem = 1
while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    #cave = [[5, 5, 4], [3, 9, 1], [3, 2, 7]]
    INF = int(1e9)
    dp = [[INF for _ in range(n)] for _ in range(n)]
    move(0, 0, problem)
    problem += 1