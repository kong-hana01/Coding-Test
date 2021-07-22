# https://www.acmicpc.net/problem/16235
# 접근방법
# 1. 두 개의 이중 리스트를 만든 뒤 하나의 리스트에는 나무의 나이를 입력한다. 나머지 리스트에는 각 나무가 있는 위치에 양분을 입력한다.
# 2. 처음에는 주어진 위치를 모두 탐색하며 해당 위치의 양분과 나이가 어린 순서로 나무들의 나이를 비교해 양분을 먹고 나이를 증가시킨다.
# 2-1. 이때 양분이 어떤 나무의 나이보다 작을 경우는 양분을 빼지 않고, 그 나무를 포함한 이후의 나무들은 모두 죽는다.
# 3. 2-1에서 죽은 나무들은 모두 절반으로 나눈 뒤(소수점 제거) 이를 합하여 해당 위치에 저장한다.
# 4. 나무의 나이가 5의 배수일 경우 자신을 둘러싼 상하좌우대각선 위치에 나무를 번식시킨다.
# 5. 모든 리스트에 대해 주어진 양분만큼의 값을 더한다.
# 6. 2-5의 과정을 k번 반복한다.
from collections import deque
n, m, k = map(int, input().split())
nourishment_add = [list(map(int, input().split())) for _ in range(n)]
trees = [[deque([]) for _ in range(n)] for _ in range(n)]
nourishment_place = [[5 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age)

def sprint_summer(n):
    for col in range(n):
        for row in range(n):
            if trees[col][row]:
                for i in range(len(trees[col][row])):
                    if trees[col][row][i] <= nourishment_place[col][row]:
                        nourishment_place[col][row] -= trees[col][row][i]
                        trees[col][row][i] += 1
                    else:
                        nourishment = 0
                        count = 0
                        for j in range(i, len(trees[col][row])):
                            nourishment += trees[col][row][j] // 2
                            count += 1
                        # nourishment_place[col][row] += sum([x//2 for x in trees[col][row][i:]]) deque 인덱스 사용 불가
                        nourishment_place[col][row] += nourishment
                        # trees[col][row] = trees[col][row][:i] deque 인덱스 사용 불가
                        for j in range(count):
                            trees[col][row].pop()
                        break

def autumn_winter(n):
    for col in range(n):
        for row in range(n):
            if trees[col][row]:
                for i in range(len(trees[col][row])):
                    if trees[col][row][i] % 5 == 0:
                        for dcol, drow in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                            if 0<=col+dcol<=n-1 and 0<=row+drow<=n-1:
                                trees[col+dcol][row+drow].appendleft(1)
            nourishment_place[col][row] += nourishment_add[col][row]


for year in range(k):
    sprint_summer(n)
    autumn_winter(n)


result = 0
for col in range(n):
    for row in range(n):
        result += len(trees[col][row])
print(result)