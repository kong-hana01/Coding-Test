# https://www.acmicpc.net/problem/1987
# 골드 문제
# 접근 방법
# DFS로 탐색하되, 방문처리는 set을 사용해 알파벳을 추가하는 방식으로 한다.
# set의 in 연산자의 시간복잡도 : O(1) -> 하지만 더 오래걸리기에 visited 리스트의 인덱스를 통해 확인하도록 함


# 첫번째 시도
# 문자를 인덱싱을 통해 탐색 -> 리스트 데이터로 바꿔 인덱싱을 통해 탐색
# 시간이 줄었지만 시간초과

# 두번째 시도
# sys.exit()을 사용해 빠른 탈출
# 25개까지인 경우는 해당사항 없으므로 시간 초과

# 세번째 시도
# visited 인덱스를 통한 탐색
# 성공

import sys
input = sys.stdin.readline
r, c = map(int, input().split())
array = [[x for x in input().rstrip()] for _ in range(r)]
visited = [0] * 26 # 방문처리를 위한 리스트 초기화
direction = [[-1, 0], [1, 0], [0, 1], [0, -1]] # 움직일 수 있는 방향(동서남북)
result = 0

def dfs(x, y, count):
    global result
    # print('x: ', x)
    # print('y: ', y)
    # print('count: ', count)
    visited[ord(array[x][y]) - ord('A')] = 1 # 해당 위치 방문처리 (A를 기준으로 인덱스 시작)
    count += 1
    for dx, dy in direction:
        if 0<=x+dx<=r-1 and 0<=y+dy<=c-1 and visited[ord(array[x+dx][y+dy]) - ord('A')] == 0:
            dfs(x+dx, y+dy, count)
    result = max(result, count) # 최대 이동한 칸을 찾기위한 result 값과 count를 비교해서 저장
    if result == 26:
        print(result)
        sys.exit()
    visited[ord(array[x][y]) - ord('A')] = 0

dfs(0, 0, 0)
print(result)