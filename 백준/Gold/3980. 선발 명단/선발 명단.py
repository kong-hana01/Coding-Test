# https://www.acmicpc.net/problem/3980
# 접근 방법
# 백트랙킹을 사용해 문제를 해결한다.
# 52분
def backtracking(i, now_score):
    # i번째 플레이어 넣기
    if not promising(now_score):
        return False
    if i == 11:
        global max_score
        max_score = max(max_score, now_score)
        return 

    for j in players_position[i]:
        if not j in position:
            position.add(j)
            backtracking(i+1, now_score+board[i][j])
            position.remove(j)
    
    return False


def promising(now_score):
    global max_score
    for x in (enable_position - position):
        now_score += promising_score[x]
    if max_score < now_score:
        return True
    return False

c = int(input())
for _ in range(c):
    board = [list(map(int, input().split())) for _ in range(11)]
    players_position = [[] for _ in range(11)]
    position = set([])
    enable_position = set([i for i in range(11)])
    promising_score = [0 for _ in range(11)]
    max_score = 0
    for i in range(11):
        for j in range(11):
            x = board[i][j]
            if x == 0:
                continue
            players_position[i].append(j)
            promising_score[j] = max(promising_score[j], x)
    backtracking(0, 0)
    print(max_score)