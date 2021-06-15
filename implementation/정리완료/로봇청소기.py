import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


# 진행 방향을 인덱스로 하고, 이동하는 값을 원소로 갖는 리스트
# 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
left_step = [[0, -1], [-1, 0], [0, 1], [1, 0]]
count = 0

while True:
    # 현재 위치가 청소를 하지 않은 공간이면 청소해주기
    if map_[r][c] == 0:    
        map_[r][c] = 2
        count += 1

    # 2-a조건 : 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    # 2-b조건 : 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    for i in range(4):
        dr, dc = left_step[d]
        d -= 1
        if d < 0:
            d = 3
        if map_[r+dr][c+dc] == 0:
            r += dr
            c += dc
            break

    # 2-c조건 : 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    # 2-d조건 : 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
    if i == 3 and map_[r][c] != 0:
        back = d - 1
        if back < 0:
            back += 4
        dr2, dc2 = left_step[back]

        # 뒷쪽 방향이 벽인 경우
        if map_[r+dr2][c+dc2] == 1:
            print(count)
            break 
        else:
            r += dr2
            c += dc2
