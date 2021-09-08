# https://www.acmicpc.net/problem/2665
# 접근 방법 1: 개수를 count에 저장해가며 저장된 값을 비교하며 진행한다.
# 현재 위치에서 검은색을 흰색으로 바꾼 누적 횟수를 최소 힙에 삽입하고 삭제하면서 BFS를 진행한다.
# 시간 소요: 80ms
def move(x, y):
    INF = int(1e9)
    count = [[INF for _ in range(n)] for _ in range(n)]
    q = []
    heapq.heappush(q, [0, x, y])
    while q:
        c, row, col = heapq.heappop(q)
        if count[row][col] < c:
            continue
        
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=row+dr<=n-1 and 0<=col+dc<=n-1:
                if board[row+dr][col+dc]:
                    cost = c
                else:
                    cost = c+1
                
                if count[row+dr][col+dc] > cost:
                    count[row+dr][col+dc] = cost
                    heapq.heappush(q, [cost, row+dr, col+dc])
                    if row+dr == n-1 and col+dc == n-1:
                        print(count[row+dr][col+dc])
                        return
                    
import heapq
n = int(input())
board = [[int(x) for x in input()] for _ in range(n)]
move(0, 0)

# 접근 방법 2: 방문처리만 하며 진행한다.
# 시간소요: 96ms
def move(x, y):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = []
    heapq.heappush(q, [0, x, y])
    while q:
        c, row, col = heapq.heappop(q)
        visited[row][col] = True

        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0<=row+dr<=n-1 and 0<=col+dc<=n-1 and not visited[row+dr][col+dc]:
                if board[row+dr][col+dc]:
                    cost = c
                else:
                    cost = c+1
                
                visited[row+dr][col+dc] = True # 모든 방향에서 해당 지점으로 오기 위한 간선의 비용이 같고, 가장 최소한으로 검은 방을 움직인 순서대로 움직이기에 상하좌우를 탐색할 때 방문처리 가능
                heapq.heappush(q, [cost, row+dr, col+dc])
                if row+dr == n-1 and col+dc == n-1:
                    print(cost)
                    return
                    
import heapq
n = int(input())
board = [[int(x) for x in input()] for _ in range(n)]
move(0, 0)