# https://www.acmicpc.net/problem/17825
# 접근 방법
# 주사위 윷놀이를 다음과 같은 리스트로 초기화한다.
# board = [[5의 배수가 아닌 인덱스인 경우의 맵], [5의 배수이자, 몫이 1인 경우 이동하게될 맵], [5의 배수이자, 몫이 2인 경우 이동하게될 맵], [5의 배수이자, 몫이 3인 경우 이동하게될 맵]]]
# 초기 말의 위치는 모두 [0, 0]로 초기화한다. ([5의 배수일 경우의 현재 위치를 5로 나눈 몫(5의 배수가 아니면 0), 현재 위치])
# board에서 5의 배수가 아닌 인덱스로 이동할 경우 말의 현재 위치만 변경시켜주고, 값을 더해준다.
# board에서 5의 배수인 인덱스로 이동할 경우 [5로 나눴을 때의 몫, 0]으로 말의 위치를 초기화한다.
# 말을 매번 이동시킬 때는 다음과 같은 주의사항을 지킨다.
# 1. 서로 다른 말들의 위치를 확인한 뒤, 말의 위치가 겹치지 않도록 한다.(고유한 번호를 통해 비교)
# 2. 현재위치를 기반으로 5의 배수인 인덱스로 이동할 때 말의 위치를 나타내는 리스트의 첫번째 인덱스가 0인 경우에만 말의 위치를 [5로 나눴을 때의 몫, 0]으로 초기화시키고, 그 외엔 초기화시키지 않고 현재 위치만 변경한다.

def move_horse(horse, number, count, score):
    if count == 11:
        global result
        result = max(score, result)
        return
    
    h = horse[number]
    if h[0] == -1:     # 이미 도착한 말을 움직이려할 때는 리턴
        return

    m = dice[count-1] # 이동 횟수 초기화
    if not (h[1] + m) % 5 and not h[0] and (h[1] + m) // 5 < 4: # 이동하고자하는 곳이 5의 배수이며 h[0]의 값이 0이라면
        next = [(h[1] + m) // 5, 0]
    else:
        if len(board[h[0]]) > h[1] + m:
            next = [h[0], h[1]+m]
        else:
            next = [-1, -1]
    
    # 말을 이동 시 서로 다른 말의 위치와 겹치는 지 확인
    if next[0] != -1:
        s = board[next[0]][next[1]]
        # print(s)
        for i in range(4):
            h_ = horse[i]
            if h_[0] != -1 and s[1] == board[h_[0]][h_[1]][1]:
                return
    
        score += s[0] # 말이 이동할 수 있는 장소일 경우 점수를 더한다.(도착지점 제외)
    
    horse_ = [x[:] for x in horse]
    horse_[number] = next
    move_horse(horse_, 0, count+1, score)
    move_horse(horse_, 1, count+1, score)
    move_horse(horse_, 2, count+1, score)
    move_horse(horse_, 3, count+1, score)
    return

dice = list(map(int, input().split()))
board = [[[i * 2, i] for i in range(21)]]
board.append([[10, 5], [13, 21], [16, 22], [19, 23], [25, 29], [30, 30], [35, 31], [40, 20]])
board.append([[20, 10], [22, 24], [24, 25], [25, 29], [30, 30], [35, 31], [40, 20]])
board.append([[30, 15], [28, 26], [27, 27], [26, 28], [25, 29], [30, 30], [35, 31], [40, 20]])
horse = [[0, 0] for _ in range(4)]
result = 0
move_horse(horse, 0, 1, 0)
print(result)