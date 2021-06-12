from collections import deque

n, m = 4, 5
#condition = [list(map(int, input().split())) for _ in range(n)]
condition = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 0]]
"""
0 0 1 1 0
0 0 0 1 1
1 1 1 1 1
0 0 0 0 0
"""



def bfs(row, col):
    """col, row : 시작 지점에 대한 행 열"""

    
    # 입력된 값이 0일 때, 즉 얼음을 만들 수 있는 공간일 때
    if condition[row][col] == 0:
        # 큐 생성
        queue = deque([[row, col]])
        # 방문 지점 표시
        condition[row][col] = 1
        # queue가 없어질 때까지 반복 후 없어지면 값을 1 추가하고 break
        while True:
            if not queue:
                return 1
                
            row, col = queue.popleft()
            # 상하좌우로 이동하며 이동한 장소가 0일 떄 큐에 추가
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                # 이동한 장소가 주어진 범위 이내인 지 확인
                if 0 <= row+dy <= n-1 and 0 <= col+dx <= m-1:  
                    if condition[row+dy][col+dx] == 0:
                        queue.append([row+dy, col+dx])
                        # 방문 지점 표시
                        condition[row+dy][col+dx] = 1

    return 0

result = 0
for row in range(len(condition)):
    for col in range(len(condition[row])):
        result += bfs(row, col)

print(result)