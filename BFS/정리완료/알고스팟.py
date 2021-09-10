# 접근 방법
# 0. 주어진 위치를 입력받는다.
# 1. 현재 위치에서 상하좌우 중 이동할 수 있는 위치를 확인하여 1을 거치면 1을 거친 횟수에 1을 더한 뒤, [1을 거친 횟수, 현재 위치]의 형태로 min_heap에 저장한다.
# 2. 이후 min_heap에서 값을 하나씩 삭제하며 1번을 반복한다.
# 3. 상하좌우의 위치를 탐색하다 (n, m)의 위치가 나오면 탐색을 멈추고 1을 거친 횟수를 출력한다. 
import sys, heapq
input = sys.stdin.readline
m, n = map(int, input().split())
board = [[int(x) for x in input().rstrip()] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def move(row, col):
    q = []
    heapq.heappush(q, [0, row, col])
    
    while q:
        count, r, c = heapq.heappop(q)
        if visited[r][c]:
            continue
            
        visited[r][c] = True
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=r+dr<=n-1 and 0<=c+dc<=m-1 and not visited[r+dr][c+dc]:
                if board[r+dr][c+dc]:
                    heapq.heappush(q, [count+1, r+dr, c+dc])
                else:
                    if r+dr == n - 1 and c+dc == m - 1:
                        return count
                    heapq.heappush(q, [count, r+dr, c+dc])
    return 0

result = move(0, 0)
print(result)