import sys, copy
sys.setrecursionlimit(15000) # NxN 크기에서 N이 최대 100이기때문에 최대 10000번 재귀함수가 돌아가기때문에 이를 해제

n = int(sys.stdin.readline()) # 크기 입력받기
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 지역별 높이 입력받기
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 방향 리스트
height_sets = set() # 최소 높이와 최대 높이의 크기 차이가 많이나고, 각 지역별 크기 차이가 심할 경우 최소 높이와 최대 높이를 기준으로 탐색 시, 너무 많은 시간이 낭비될 수 있기에 set으로 처리

# height_sets에 높이 추가
for i in range(n):
    for j in range(n):
        height_sets.add(graph[i][j])


# DFS를 통한 안전 지역 체크
def check_safe_zone(row, col, height):
    map_[col][row] = 0 # 방문 처리 0

    # 상하좌우 네 방향으로 탐색
    for dcol, drow in direction:
        new_col, new_row = col+dcol, row+drow
        if 0<=new_col<=n-1 and 0<=new_row<=n-1 and map_[new_col][new_row] > height: # 행렬 모두 주어진 범위 이내인지, 현재 탐색하고자하는 높이보다 높은 지 확인
            check_safe_zone(new_row, new_col, height)

countOfsafezone = 1 # 최소 안전 범위 = 1 (모든 지역이 가라앉지 않는 경우, 만약 최소 높이를 낮춰 탐색할 경우 최대 10000번의 탐색이 추가로 요구되기에 이를 피하기위해 최소 높이를 사전에 설정)
for height in height_sets: # 주어진 높이에 대해서 탐색
    count = 0
    map_ = copy.deepcopy(graph) # 매 방문 처리 초기화를 위한 deepcopy
    for col in range(n):
        for row in range(n):
            if map_[col][row] > height: # 현재 높이보다 높을 경우 DFS 탐색 시작
                check_safe_zone(row, col, height)
                count += 1

    countOfsafezone = max(countOfsafezone, count) # 최대 높이를 구하기 위해 현재까지의 안전지역의 최대값과, 방금 탐색한 안전지역의 개수 중 큰 값을 저장

print(countOfsafezone) # 최대 안전 지역의 개수 출력