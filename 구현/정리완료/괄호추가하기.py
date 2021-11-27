# https://www.acmicpc.net/problem/16637
# 접근 방법
# 괄호를 0개부터 최대 5개까지 추가하는 모든 경우의 수 중에 가장 높은 수를 출력한다.
from itertools import combinations

# 대략적인 경우의 수 개수 세기
# cases = 0
# for i in range(1, 6):
#     cases += len(list(combinations([x for x in range(1, 6)], i))) * 2 - 1
    # print(list(combinations([x for x in range(1, 6)], i)))
# print(cases) >> 57개


n = 7
array = ['8', '*', '3', '+', '5', '+', '2']
for i in range(0, n, 4):
    if i + 2 <= n-1:
        for j in range(i, n, 4):
            if i != j and j + 2 <= n-1:
                print(i, j)
                
for i in range(2, n, 4):
    if i + 2 <= n-1:
        print(i)
        for j in range(i, n, 4):
            if i != j and j + 2 <= n-1:
                print(i, j)