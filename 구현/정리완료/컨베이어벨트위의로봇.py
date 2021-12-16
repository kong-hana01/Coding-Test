# https://www.acmicpc.net/problem/20055
# 접근 방법
# 다음과 같이 주어진 순서에 따라 동작하게끔 코드를 작성한다.
# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
# 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

n, k = map(int, input().split())
durability = list(map(int, input().split()))
conveyor_belt = [0 for _ in range(n*2)]
def rotate():
    # 컨베이어 벨트를 한 칸 움직인다.    
    for i in range(n*2-1, 0, -1):
        conveyor_belt[i], conveyor_belt[i-1] = conveyor_belt[i-1], 0
        durability[i], durability[i-1] = durability[i-1], durability[i]
    
    conveyor_belt[n-1] = 0
    conveyor_belt[0] = 0

def move():
    # 로봇을 이동시킨다.
    global count
    for i in range(n*2-1, 0, -1):
        if conveyor_belt[i-1] == 1 and conveyor_belt[i] == 0 and durability[i] >= 1:
            conveyor_belt[i], conveyor_belt[i-1] = conveyor_belt[i-1], 0
            durability[i] -= 1
            if durability[i] == 0:
                count += 1
    conveyor_belt[n-1] = 0

def put_up():
    # 로봇을 올린다.
    global count 
    if durability[0] >= 1:
        conveyor_belt[0] = 1
        durability[0] -= 1
        if durability[0] == 0:
            count += 1

count = 0
step = 0
while count < k:
    rotate()
    move()
    put_up()
    step += 1
    # print('내구도:', durability)
    # print('컨베이어 벨트:', conveyor_belt)
    # print()
print(step)