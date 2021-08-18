# https://www.acmicpc.net/problem/17837
# 접근 방법
# 0. 주어진 체스판을 입력받은 뒤(board), 체스판의 크기와 동일하고 빈 리스트를 값으로 가지는 리스트(horseOnBoard)를 초기화한다. 말의 정보는 그대로 입력받는다. (horse)
# 1. horseOnBoard에 말의 번호를 차례로 입력한다.
# 2. horse를 하나씩 탐색하며 말을 이동시킨다. 이동시킬 때는 horseOnBoard에 저장되어있는 말 번호 중 이동시키려는 말의 인덱스 이상의 리스트(horse_array)를 모두 이동 위치에 append하여 이동시킨다.
# 2-1. horse가 이동하려는 위치가 흰색(0)이라면 그 위치로 이동시킨다.
# 2-2. horse가 이동하려는 위치가 빨간색(1)이라면 현재 horse_array를 모두 뒤집은 뒤, 이를 그 위치로 이동시킨다.
# 2-3. horse가 이동하려는 위치가 파란색(2)이거나 체스판의 범위를 벗어나면 이동방향을 반대로 하고 한 칸 이동한다. 만약 이동하려는 칸이 파란색인 경우는 이동하지 않는다.
# 3. horse를 이동시킨 뒤, horse_array에 있는 모든 말의 위치를 horse에서 현재 위치로 바꾼다.
# 4. horse을 이동한 위치의 horseOnBoard의 리스트의 길이가 4 이상이 될 때까지 2 ~ 3번을 반복한다.

# 0. 주어진 정보 입력
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
horse = []
step = [0, [0, 1], [0, -1], [-1, 0], [1, 0]]
for _ in range(k):
    r, c, d = map(int, input().split())
    horse.append([r-1, c-1, d])
horseOnBoard = [[[] for _ in range(n)] for _ in range(n)]

# 1. horseOnBoard에 말 번호 저장
for i in range(k):
    r, c, d = horse[i]
    horseOnBoard[r][c].append(i)



def move(number, horseOnBoard):
    r, c, d = horse[number]
    # 2. 이동시키려는 여러 개의 말 번호를 horse_array로 저장
    for i in range(len(horseOnBoard[r][c])):
        if horseOnBoard[r][c][i] == number:
            horse_array = horseOnBoard[r][c][i:] # horse_array: 말번호 저장
            horseOnBoard[r][c] = horseOnBoard[r][c][:i]
            break
    
    dr, dc = step[d]
    if 0<=r+dr<=n-1 and 0<=c+dc<=n-1 and board[r+dr][c+dc] < 2:
        
        # 2-1. 이동하려는 위치가 흰색인 경우 쌓여있는 순서를 바꾼 빨간색인 경우와 동일
        # 2-2. 이동하려는 위치가 빨간색인 경우
        if board[r+dr][c+dc] == 1:
            horse_array = horse_array[::-1]
        # 3. 말의 위치 입력
        for num in horse_array:
            horseOnBoard[r+dr][c+dc].append(num)
            horse[num][0] = r+dr
            horse[num][1] = c+dc
        
        return len(horseOnBoard[r+dr][c+dc])

    # 2-3. 이동하려는 위치가 파란색인 경우
    else:
        if d in [1, 3]:
            d += 1
        else:
            d -= 1
            

        dr, dc = step[d]
        horse[number][2] = d
        if 0<=r+dr<=n-1 and 0<=c+dc<=n-1 and board[r+dr][c+dc] < 2:
            
            if board[r+dr][c+dc] == 1:
                horse_array = horse_array[::-1]
            for num in horse_array:
                horseOnBoard[r+dr][c+dc].append(num)
                horse[num][0] = r+dr
                horse[num][1] = c+dc

            return len(horseOnBoard[r+dr][c+dc])
        else:
            for num in horse_array:
                horseOnBoard[r][c].append(num)
            
            return len(horseOnBoard[r][c])
   

turn = 1
while turn <= 1000:
    count = 0
    for i in range(k):
        count = max(move(i, horseOnBoard), count)

    if count >= 4:
        break
    turn += 1

if count >= 4:
    print(turn)
else:
    print(-1)
