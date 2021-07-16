# https://www.acmicpc.net/problem/15684
# 접근 방법
# 1. 주어진 세로선 + 1과 가로선을 놓을 수 있는 위치 + 1 만큼의 이중리스트를 2개 만든다.
# 1-1. 사다리를 놓는 이중 리스트와 값이 내려가는 리스트를 구분해 사다리를 놓는 리스트에는 주어진 가로선을 입력한다.
# 2-1. 아직 사다리가 놓이지 않은 곳에 대해 경우의 수를 늘려가며 주어진 조건을 통과하는지 확인한다.
# 2-2. 문제 조건을 만족하기 위해서는 세로 선에 짝수개만큼 가로선이 놓여있어야한다. 따라서 가로선이 홀수인 세로선의 개수가 2개를 초과하면 해당 세로선에 대해서만 경우의 수를 늘려간다.
# 2-3. 
# 보류

from itertools import combinations
count = 0
for i in list(combinations([x for x in range(1, 265)], 1)):
    for j in list(combinations([x for x in range(1+i[0], 263)], 1)):
        for k in list(combinations([x for x in range(1+i[0]+j[0], 261)], 1)):
            count += 1

print(count)
# print(len(list(combinations([x for x in range(1, 268)], 3))))