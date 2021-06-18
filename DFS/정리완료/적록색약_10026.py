import sys, copy
from collections import deque
sys.setrecursionlimit(10**6) # 재귀 깊이가 최대 100x100 = 10000이 될 수 있기에 재귀 깊이를 늘려준다.

n = int(sys.stdin.readline())
painting = [sys.stdin.readline().rstrip() for _ in range(n)]
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(row, col, target):
    """ 
    row : 그림의 row
    col : 그림의 col
    target : 탐색하고자하는 색깔 ('R', 'G', 'B')
    """
    visited[col][row] = True # 현재 위치 방문 처리
    for drow, dcol in direction: # 상하좌우에 대한 방향 받기
        new_row = row+drow
        new_col = col+dcol
        # 현재위치의 상하좌우에 해당하는 위치가 주어진 범위 이내인지, 아직 방문하지 않았는지, 탐색하고자 하는 색깔인지 파악 후 모두 맞을 경우, DFS탐색
        if 0<=new_row<=n-1 and 0<=new_col<=n-1 and not visited[new_col][new_row] and painting_[new_col][new_row] == target:
            dfs(new_row, new_col, target)


# 적록색약이 아닌 경우, 적록 색약인 경우로 나누어 실행
for red_green_blindness in [False, True]: 
    painting_ = copy.deepcopy(painting) # 적록색약의 경우 painting의 값을 바꿔야하기에 이를 deepcopy한다.
    visited = [[False for _ in range(n)] for _ in range(n)] # 방문 처리를 위한 리스트
    count = 0 # 구역의 수 초기화
    if red_green_blindness:
        for i in range(n):
            painting_[i] = painting[i].replace('G', 'R')  # 적록색약의 경우 G -> R로 값 변경

    # R, G, B에 대해 한번씩 탐색한다.
    for target in ['R', 'G', 'B']:
        for col in range(n):
            for row in range(n):
                if not visited[col][row] and painting_[col][row] == target: # 아직 방문하지 않은 위치이고, 탐색하고자하는 색깔일 때 DFS 탐색 시작
                    dfs(row, col, target)
                    count += 1 # 한 구역에 대한 DFS 탐색이 완료되면 카운트 증가
    print(count)