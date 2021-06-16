import sys
sys.setrecursionlimit(10**6)

# 상하좌우 대각선 까지 총 8개의 방향 설정
direction = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]

# 깊이 우선 탐색 함수 정의
def dfs(row, col):
    """
    row : 가로 인덱스
    col : 세로 인덱스
    """
    # 방문한 지역은 0으로 값을 바꿔준다.
    graph[col][row] = 0

    # 현재 위치에서 상하좌우대각선 위치 탐색
    for dcol, drow in direction: 
        new_col = col+dcol
        new_row = row+drow
        # 현재 지도의 범위를 벗어나지 않으면서 섬이 있는 지역을 탐색
        if 0 <= new_col <= h-1 and 0 <= new_row <= w-1 and graph[new_col][new_row] == 1: 
            dfs(new_row, new_col)

# w, h값이 0, 0일 때까지 반복
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == h == 0:
        break
    # 가로길이가 w이고, 세로 길이가 h인 지도 리스트 초기화
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    countOfisland = 0 # 섬의 개수 초기화
    for col in range(h):
        for row in range(w):
            if graph[col][row] == 1: 
                dfs(row, col) # 해당 col과 row와 연결된 섬의 개수를 모두 찾고 개수는 +1
                countOfisland += 1
    print(countOfisland)