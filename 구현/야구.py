# https://www.acmicpc.net/problem/17281
# 접근 방법
# 선수의 순서의 모든 경우의 수에 대해 리스트로 만든 뒤, 각 이닝 별로 점수를 계산해 이를 출력한다.
# 이때 선수의 순서를 만드는 함수와 이닝별로 점수를 계산하는 함수를 분할하여 문제를 해결한다.
# 1번째 선수는 항상 4번째에 위치해있어야하는 것에 주의해 선수의 순서를 만든다.
# 삼성 sw
def play(roster):
    global maxScore
    score = 0
    order = 0
    for inning in innings:
        outCount = 0
        b3, b2, b1 = 0, 0, 0
        while outCount < 3:
            result = inning[roster[order]]
            order = order + 1 if order < 8 else 0

            if result == 0:
                outCount += 1

            elif result == 1:
                score += b3
                b3, b2, b1 = b2, b1, 1

            elif result == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0

            elif result == 3:
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0

            elif result == 4:
                score += b1 + b2 + b3 + 1
                b3, b2, b1 = 0, 0, 0

    maxScore = max(score, maxScore)

from itertools import permutations
n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
maked = [False for _ in range(10)]
maxScore = 0
cases = permutations((1, 2, 3, 4, 5, 6, 7, 8))
for case in cases:
    play(case[:3] + (0,) + case[3:])
print(maxScore)