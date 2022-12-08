# https://www.acmicpc.net/problem/2174
# 접근 방법
# 명령어를 수행하는 함수, 움직이는 함수, 회전하는 함수를 각각 만들어서 문제를 해결한다.
def input_command(robot_number, command, count):
    if command == 'F':
        return move(robot_number, count)
    x, y = location_of_robots[robot_number]
    direct = board[x][y]
    for _ in range(count):
        direct = rotate(direct, command)
    board[x][y] = direct
    return [True]

def move(robot_number, count):
    x, y = location_of_robots[robot_number]
    direct = board[x][y]
    board[x][y] = 0
    step = step_of_direct[direct]
    dx, dy = step
    for _ in range(count):
        x += dx
        y += dy
        if not (1<=x<=b and 1<=y<=a):
            return [False, f"Robot {robot_number} crashes into the wall"]
        if board[x][y] != 0:
            other = location_of_robots.index([x, y])
            return [False, f"Robot {robot_number} crashes into robot {other}"]
    location_of_robots[robot_number] = [x, y]
    board[x][y] = direct
    return [True]

def rotate(direct, command):
    if command == "L":
        if direct == "N":
            return "W"
        elif direct == "W":
            return "S"
        elif direct == "S":
            return "E"
        return "N"
    if direct == "N":
        return "E"
    elif direct == "E":
        return "S"
    elif direct == "S":
        return "W"
    return "N"

a, b = map(int, input().split())
n, m = map(int, input().split())
board = [[0 for _ in range(a+1)] for _ in range(b+1)]
location_of_robots = [[]] # 로봇은 1번부터 시작하기에 이를 맞춰주기 위함
step_of_direct = {"N": [-1, 0], "W": [0, -1], "E": [0, 1], "S": [1, 0]}

for _ in range(n):
    x, y, direct = input().split()
    board[b-int(y)+1][int(x)] = direct
    location_of_robots.append([b-int(y)+1, int(x)])

is_success = True
commands = [input().split() for _ in range(m)]
for robot_number, command, count in commands:
    result = input_command(int(robot_number), command, int(count))
    if not result[0]:
        is_success = False
        print(result[1])
        break

if is_success:
    print("OK")