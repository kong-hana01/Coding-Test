# https://www.acmicpc.net/problem/15684
# 접근 방법
# 1. 주어진 세로선 + 1과 가로선을 놓을 수 있는 위치 + 1 만큼의 이중리스트를 2개 만든다.
# 1-1. 사다리를 놓는 이중 리스트와 값이 내려가는 리스트를 구분해 사다리를 놓는 리스트에는 주어진 가로선을 입력한다.
# 2-1. 아직 사다리가 놓이지 않은 곳에 대해 경우의 수를 늘려가며 주어진 조건을 통과하는지 확인한다.
# 2-2. 문제 조건을 만족하기 위해서는 세로 선에 짝수개만큼 가로선이 놓여있어야한다. 따라서 가로선이 홀수인 세로선의 개수가 2개를 초과하면 해당 세로선에 대해서만 경우의 수를 늘려간다.
# 2-3. 
# 보류
import time
from collections import deque
n, h = 10, 30
plane = [[0 for _ in range(n+1)] for _ in range(h+1)]
# array = [[1, 1], [3, 2], [2, 3], [5, 1], [5, 4]]
# for i, j in array:
#     plane[i][j], plane[i][j+1] = 1, 1
for i in range(n):
    plane[0][i] = i

from itertools import combinations
count = 0
start = time.time()
def find_ladder(plane):
    ladder = []
    for i in range(1, h+1):
        for j in range(1, n):
            if plane[i][j] != 1 and plane[i][j+1] != 1:
                ladder.append([i, j])
    return ladder


# ladder = find_ladder(plane)
# for i in range(len(ladder)):
#     plane_ = [x[:] for x in plane]
#     ladder_ = ladder[:]
#     x1, y1 = ladder[i]
#     plane_[x1][y1], plane_[x1][y1+1] = 1, 1
#     for j in range(i+1, len(ladder_)):
#         if ladder_[i][1] + 1 == ladder_[j][1] and ladder_[i][0] == ladder[j][0]:
#             continue
#         x2, y2 = ladder_[j]
#         plane_[x2][y2], plane_[x2][y2+1] = 1, 1
#         for k in range(j+1, len(ladder_)):
#             if (ladder_[j][1] + 1 == ladder_[k][1] and ladder_[j][0] == ladder[k][0]) or (ladder_[i][1] + 1 == ladder_[k][1] and ladder_[i][0] == ladder[k][0]):
#                 continue
#             count += 1
#             # print(i, j, k)
#         plane_[x2][y2], plane_[x2][y2+1] = 0, 0
    
# print(count)
# print(time.time()-start)





# ladder = find_ladder(plane)
# for i in range(len(list(combinations(ladder, 1)))):
#     plane_ = plane[:]
#     ladder_ = ladder[:]
#     # x, y = ladder[i]
#     # plane_[x][y], plane_[x][y+1] = 1, 1
#     # ladder_ = find_ladder(plane_)
#     for j in range(i+1, len(list(combinations(ladder, 1)))):
#         # x, y = ladder[j]
#         # plane_[x][y], plane_[x][y+1] = 1, 1
#         # ladder_ = find_ladder(plane_)
#         for k in range(j+1, len(list(combinations(ladder, 1)))):
#             count += 1
#             # print(i, j, k)
# print(time.time()-start)
# ladder = find_ladder(plane)
# for i in range(len(ladder)):
#     plane_ = [x[:] for x in plane]
#     ladder_ = ladder[:]
#     x1, y1 = ladder[i]
#     plane_[x1][y1], plane_[x1][y1+1] = 1, 1
#     ladder_ = find_ladder(plane_)
#     j = i + 1
#     while j <= len(ladder_) - 1:
#         x2, y2 = ladder_[j]
#         plane_[x2][y2], plane_[x2][y2+1] = 1, 1
#         ladder_ = find_ladder(plane_)
#         k = j + 1
#         while k <= len(ladder_) - 1:
#             count += 1
#             # print(i, j, k)
#             k += 1
#         plane_[x2][y2], plane_[x2][y2+1] = 0, 0
#         j += 1
# print(count)