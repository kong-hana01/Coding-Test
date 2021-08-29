# https://www.acmicpc.net/problem/14889
# 접근방법
# 조합 라이브러리를 활용해 팀을 나눈 뒤, 능력치의 차이가 최소인 값을 고른다.
from itertools import combinations

# array = [x for x in range(1, 21)]
# print(len(list(combinations(array, len(array)//2))))
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        array[i][j] += array[j][i]
        array[j][i] = 0
teams = list(combinations([i for i in range(n)], n//2))
# print(teams)
d = [0] * (len(teams) // 2)
for i in range(len(teams)):
    if i < len(teams)//2:
        for j in range(n//2):
            for k in range(j+1, n//2):
                x = teams[i][j]
                y = teams[i][k]
                d[i] += array[x][y]
    else:
        for j in range(n//2):
            for k in range(j+1, n//2):
                x = teams[i][j]
                y = teams[i][k]
                d[-(i-len(teams)//2)-1] -= array[x][y]
print(min([x if x > 0 else -x for x in d]))