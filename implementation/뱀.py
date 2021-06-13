from collections import deque
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples = [list(map(int,sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline())
directions = [sys.stdin.readline().split() for _ in range(l)]


# n = 6
# k = 3
# apples = [[3, 4], [2, 5], [5, 3]]
# l = 3
# # 시간이 느린 순서대로 정렬 -> 제일 뒤의 인덱스로 확인 후 해당 시간이 지나면 pop
# directions = [['3', 'D'], ['15', 'L'], ['17', 'D']]
directions.sort(reverse=True, key=lambda x: int(x[0]))

map_ = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(k):
    x, y = apples[i]
    map_[y][x] = 1

steps = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 동/남/서/북
d = 0 # 방향 인덱스
count = 0

snake = deque([])
snake.append([1,1])

while True:
    tail = snake[0]
    head = snake[-1]
    dx, dy = steps[d] # 이동 경로 탐색
    count += 1 # 시간 체크
    

    if 1<=head[0]+dx<=n and 1<=head[1]+dy<=n:
        # 자기자신의 몸에 부딪히면 게임이 끝난다.
        if [head[0]+dx, head[1]+dy] in snake:
            break
        
        if len(directions) > 0 and count == int(directions[-1][0]):
            time, dir = directions.pop()
            if dir == 'D':
                d = (d+1) % 4
            elif dir == 'L':
                d = (d-1) % 4
        
        if map_[head[1]+dy][head[0]+dx] != 1:
            snake.popleft()
        else:
            map_[head[1]+dy][head[0]+dx] = 0


        snake.append([head[0]+dx, head[1]+dy])
        print(snake)




    # 벽에 몸에 부딪히면 게임이 끝난다.
    else:
        break
print(count)