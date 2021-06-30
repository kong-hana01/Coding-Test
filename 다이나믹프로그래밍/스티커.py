# 문제 https://www.acmicpc.net/problem/9465
# 접근방법
# 스티커를 열 방향으로 차례로 선택하면서 왼쪽 대각선에 위치한 스티커와 그 왼쪽에 있는 스티커 중 높은 값과 현재 스티커의 점수와 더한다.

import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(2)]
    # n = 5
    # array = [[50, 10, 100, 20, 40], [30, 50, 70, 10, 60]] 
    d = [[0 for _ in range(n)] for _ in range(2)] #다이나믹 프로그래밍을 위한 dp 테이블 초기화

    for i in range(2):
        d[i][0] = array[i][0] # 1열에 해당하는 dp 값 입력

    for i in range(2):
        d[i][1] = array[i][1]  + d[((i+1)%2)][0] # 2열에 해당하는 dp 값 계산

    score = 0 # 점수 초기화
    for i in range(2, n):
        for j in range(2):
            d[j][i] = array[j][i] + max(d[(1+j)%2][i-1], d[(1+j)%2][i-2]) # d의 왼쪽 대각선 스티커와 그 왼쪽에 있는 스티커 중 더 높은 값과 현재 스티커의 점수와 더한다.
            score = max(score, d[j][i]) # 가장 높은 점수 저장

    print(score)