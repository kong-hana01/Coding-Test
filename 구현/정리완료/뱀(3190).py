from collections import deque
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples = [list(map(int,sys.stdin.readline().split())) for _ in range(k)]
l = int(sys.stdin.readline())
directions = [sys.stdin.readline().split() for _ in range(l)]


# 시간이 느린 순서대로 정렬 -> 제일 뒤의 인덱스로 확인 후 해당 시간이 지나면 pop
# 시간복잡도 : O(NlogN) 소요
# 주어진 방향 전환 정보에 대해 앞에서부터 순차적으로 탐색해가며 시간이 지나면 인덱스를 증가시키는 방향으로 식을 짠다면 조금 더 빠르게 동작할 수 있다. 주어진 방향 전환 정보는 X가 증가하는 순으로 주어지기 때문이다.
#  * 파이썬에서 제공하는 정렬 함수의 시간복잡도 : O(NlogN) 
#  * 파이썬에서 리스트 삭제 시간복잡도 : pop()은 O(1) / remove()는 O(N)
#  * 파이썬에서 인덱스를 통한 탐색 시간 복잡도 : O(1)

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
    
    # 벽 안에 머리가 포함되는지 확인한다.
    if 1<=head[0]+dx<=n and 1<=head[1]+dy<=n:
        # 자기자신의 몸에 부딪히면 게임이 끝난다.
        if [head[0]+dx, head[1]+dy] in snake:
            break
        
        # 방향 전환 정보의 시간이 되면 방향을 전환한다. 주의할 점은 현재 머리의 위치는 방향 정보 시간이 되기 이전의 방향 정보를 반영해야한다는 점이다.
        if len(directions) > 0 and count == int(directions[-1][0]):
            time, dir = directions.pop()
            if dir == 'D':
                d = (d+1) % 4
            elif dir == 'L':
                d = (d-1) % 4
        
        # 사과가 없다면 snake에서 tail을 삭제한다.
        if map_[head[1]+dy][head[0]+dx] != 1:
            snake.popleft()
        # 사과가 있다면 map_에서 사과를 삭제한다.    
        else:
            map_[head[1]+dy][head[0]+dx] = 0
        snake.append([head[0]+dx, head[1]+dy])
        print(snake)

    # 벽에 몸에 부딪히면 게임이 끝난다.
    else:
        break
print(count)