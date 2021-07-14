# https://www.acmicpc.net/problem/13458
# 접근 방법
# 각 시험장에 있는 응사자의 수(Ai)에 총 감독관이 감시할 수 있는 응시자 수(B)를 빼고 이를 부감독관이 감시할 수 있는 응시자 수만큼 나눠준뒤, 올림을 한다.
# 모든 시험장에 대해서 위와 같이 반복하고 총 감독관의 수를 구한다.
# 각 시험장마다의 감독관 수: ((Ai - B) / C)의 올림 + 1

import sys
n = int(input())
array = list(map(int, sys.stdin.readline().split()))
b, c = map(int, input().split())

result = 0
for x in array:
    x -= b
    if x > 0:
        result += x // c + 1
        if x % c != 0:
            result += 1
    else:
        result += 1
print(result)