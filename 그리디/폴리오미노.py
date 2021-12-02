# https://www.acmicpc.net/problem/1343
# 접근 방법
# 0. 보드판을 차례로 탐색하며 .이 나오기 전 X의 개수를 더한다.
# 1. .이 나온다면 X의 개수가 2의 배수인지, 4의 배수인지 확인해, 4의 배수라면 그 몫만큼 AAAA를 넣어주고, 나머지의 2의 배수 여부를 확인해 BB를 넣어준다.
# 2. 모든 탐색이 끝나고 결과를 출력한다.
board = input()
def polyomino(board):
    result = ''
    countX = 0
    for x in board:
        if x == '.':
            if countX % 2:
                return -1
            result = result + (countX // 4 * 'AAAA') + ((countX % 4) // 2 * "BB") + '.'
            countX = 0
            
        else:
            countX += 1

    if countX % 2:
        return -1
    result = result + (countX // 4 * 'AAAA') + ((countX % 4) // 2 * "BB")
    return result

print(polyomino(board))