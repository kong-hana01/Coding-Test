n = int(input())
plan = list(map(int, input().split()))

#맵 만들기
map = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        map.append(i, j)

#이동 조건 만들기
walk = {'R' : (0, 1), 'L' : (0, -1), 'U' : (-1, 0), 'D' : (1, 0)}

# 이동
x = y = 1
for action in plan:
    dx, dy = walk[action]
    if [x+dx, y+dy] in map:
        x = x+dx
        y = y+dy
print(x, y)