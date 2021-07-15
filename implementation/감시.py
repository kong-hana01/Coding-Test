# https://www.acmicpc.net/problem/15683
# 접근방법
# 주어진 cctv의 방향에 대한 경우의 수를 모두 고려한 뒤 각 경우의 수 마다 사각지대의 크기를 구한다.
# 이때 가장 작은 사각지대의 크기를 출력한다.
# 시간복잡도
# 최대 연산횟수: 8(사무실의 가로 길이) x 8(사무실의 세로 길이) x 4의 8제곱(cctv의 최대 경우의 수) = 약 420만번 (시간복잡도 통과)

from itertools import combinations

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]


# 1번, 3번, 4번 cctv의 경우 총 4가지의 경우의 수가 존재
# 2번 cctv의 경우 총 2가지의 경우의 수가 존재
# 5번 cctv의 경우 총 1가지의 경우의 수가 존재
# 따라서 이러한 경우의 수를 각각 다르게 체크해야함
possibility_4 = []
possibility_2 = []
placeOfcctv = []
block = 0
for i in range(n):
    for j in range(m):
        if office[i][j] in [1, 3, 4]: # 1, 3, 4번 cctv
            for x in [1, 2, 3, 4]: # 각각 상하좌우
                possibility_4.append(x)
            placeOfcctv.append([i, j])
        elif office[i][j] == 2: # 2번 cctv
            possibility_2.append(1) # 가로
            possibility_2.append(2) # 세로
            placeOfcctv.append([i, j])
        elif office[i][j] == 5:
            placeOfcctv.append([i, j])
        elif office[i][j] == 0:
            block += 1

def move_up(cctv):
    count = 0
    i = 0
    while cctv[0] + i >= 0:
        if office_[cctv[0] + i][cctv[1]] == 0:
            office_[cctv[0] + i][cctv[1]] = 7
            count += 1
        elif office_[cctv[0] + i][cctv[1]] == 6:
            break
        i -= 1
    return count

def move_down(cctv):
    count = 0
    i = 0
    while cctv[0] + i <= n-1:
        if office_[cctv[0] + i][cctv[1]] == 0:
            office_[cctv[0] + i][cctv[1]] = 7
            count += 1
        elif office_[cctv[0] + i][cctv[1]] == 6:
            break
        i += 1
    return count

def move_left(cctv):
    count = 0
    j = 0
    while cctv[1] + j >= 0:
        if office_[cctv[0]][cctv[1] + j] == 0:
            office_[cctv[0]][cctv[1] + j] = 7
            count += 1
        elif office_[cctv[0]][cctv[1] + j] == 6:
            break
        j -= 1
    return count

def move_right(cctv):
    count = 0
    j = 0
    while cctv[1] + j <= m-1:
        if office_[cctv[0]][cctv[1] + j] == 0:
            office_[cctv[0]][cctv[1] + j] = 7
            count += 1
        elif office_[cctv[0]][cctv[1] + j] == 6:
            break
        j += 1

    return count

def move(cctv, direction=0):
    ''' 
        cctv: cctv의 위치
        direction: cctv가 바라보고 있는 방향
    '''
    place = office_[cctv[0]][cctv[1]]
    count = 0
    if place == 1:
        if direction == 1:
            count = move_up(cctv)
        elif direction == 2:
            count = move_down(cctv)
        elif direction == 3:
            count = move_left(cctv)
        else:
            count = move_right(cctv)

    elif place == 2:
        if direction == 1:
            count += move_right(cctv)
            count += move_left(cctv)
        elif direction == 2:
            count += move_up(cctv)
            count += move_down(cctv)

    elif place == 3:
        if direction == 1 or direction == 2:
            count += move_right(cctv)
        if direction == 2 or direction == 3:
            count += move_down(cctv)
        if direction == 3 or direction == 4:
            count += move_left(cctv)
        if direction == 4 or direction == 1:
            count += move_up(cctv)

    elif place == 4:
        if direction == 1:
            count += move_left(cctv)
            count += move_up(cctv)
            count += move_right(cctv)
        elif direction == 2:
            count += move_up(cctv)
            count += move_right(cctv)
            count += move_down(cctv)
        elif direction == 3:
            count += move_right(cctv)
            count += move_down(cctv)
            count += move_left(cctv)
        elif direction == 4:
            count += move_down(cctv)
            count += move_left(cctv)
            count += move_up(cctv) 
    else:
        count += move_up(cctv)
        count += move_right(cctv)
        count += move_down(cctv)
        count += move_left(cctv)
    # print(office_)
    return count

result = 64
for poss4 in set(combinations(possibility_4, len(possibility_4)//4)):
    for poss2 in set(combinations(possibility_2, len(possibility_2)//2)):
        i_4 = 0
        i_2 = 0
        office_ = [o[:] for o in office]
        count = 0
        for cctv in placeOfcctv:
            if office_[cctv[0]][cctv[1]] in [1, 3, 4]:
                count += move(cctv, poss4[i_4])
                i_4 += 1
            elif office_[cctv[0]][cctv[1]] == 2:
                count += move(cctv, poss2[i_2])
                i_2 += 1
            else:
                count += move(cctv)

        result = min(result, block-count)
        
print(result)