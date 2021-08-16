# https://www.acmicpc.net/problem/2096
# 접근 방법
# 3개의 값을 가지고 있는 dp 테이블을 두 개(min_score, max_score) 초기화한다.
# 매 줄마다 입력받은 숫자에 대해 값을 탐색하고, min_score와 max_score에 알맞게 값을 저장한다.

import sys

n = int(sys.stdin.readline())
a, b, c = map(int, sys.stdin.readline().split())
min_score, max_score = [a, b, c], [a, b, c]

for i in range(n-1):
    array = list(map(int, sys.stdin.readline().split()))
    min_temp = [0, 0, 0]
    max_temp = [0, 0, 0]

    min_temp[0] = min(min_score[0], min_score[1]) + array[0]
    max_temp[0] = max(max_score[0], max_score[1]) + array[0]

    min_temp[1] = min(min_score[0], min_score[1], min_score[2]) + array[1]
    max_temp[1] = max(max_score[0], max_score[1], max_score[2]) + array[1]

    min_temp[2] = min(min_score[1], min_score[2]) + array[2]
    max_temp[2] = max(max_score[1], max_score[2]) + array[2]
    
    min_score = min_temp
    max_score = max_temp

print(max(max_score), min(min_score))