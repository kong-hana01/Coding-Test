# 접근방법
# 톱니바퀴들의 정보를 담고 있는 이중 리스트를 만들어서 방향을 움직일 때마다 인덱스를 바꿔가며 현재의 방향 정보를 저장한다.
import copy
wheels = [[]]
for _ in range(4):
    wheels.append([int(x) for x in input()]) # 톱니바퀴 정보 담기
k = int(input())
order = [list(map(int, input().split())) for _ in range(k)]
# print(order)
# 각 톱니바퀴의 왼쪽에 해당하는 인덱스 초기화 / 오른쪽 인덱스는 (왼쪽 인덱스 + 4) % 8
d = [0, 6, 6, 6, 6]
for x in order:
    d_ = copy.deepcopy(d)
    if x[1] == 1:
        d_[x[0]] = (d_[x[0]] - 1) % 8
    else:
        d_[x[0]] = (d_[x[0]] + 1) % 8

    i = 0
    while x[0] + i < 4: # 해당 톱니바퀴의 오른쪽 탐색(오른쪽 톱니바퀴는 왼쪽 인덱스)
        # print(f'{x[0]+i}번째 톱니바퀴')
        # print('해당 톱니바퀴의 오른쪽 인덱스:', (d[x[0] + i] + 4) % 8)
        # print([x[0] + i + 1])
        # print([d[x[0] + i + 1]])

        if wheels[x[0]+ i][(d[x[0] + i] + 4) % 8] != wheels[x[0] + i + 1][d[x[0] + i + 1]]: # 현재 탐색중인 톱니바퀴의 오른쪽 인덱스 값과 그 오른쪽 톱니바퀴의 왼쪽 인덱스 값이 다른 경우(극이 다른 경우)
            if (x[1] == 1 and i % 2 == 0) or (x[1] == -1 and i % 2 == 1):
                d_[x[0] + i + 1] = (d_[x[0] + i + 1] + 1) % 8
            else:
                d_[x[0] + i + 1] = (d_[x[0] + i + 1] - 1) % 8
        else:
            break
        i += 1
        # print(d_)
    
    i = 0
    while x[0] - i - 1 > 0: # 해당 톱니바퀴의 왼쪽 탐색(왼쪽 톱니바퀴는 오른쪽 인덱스)
        # print(f'{x[0]-i}번째 톱니바퀴')
        # print('해당 톱니바퀴의 왼쪽 인덱스:', d[x[0] - i])
        # print(x[0] - i - 1)
        # print((d[x[0] - i - 1] + 4) % 8)
        if wheels[x[0] - i][d[x[0] - i]] != wheels[x[0] - i - 1][(d[x[0] - i - 1] + 4) % 8]:
            if (x[1] == 1 and i % 2 == 0) or (x[1] == -1 and i % 2 == 1):
                d_[x[0] - i - 1] = (d_[x[0] - i - 1] + 1) % 8
            else:
                d_[x[0] - i - 1] = (d_[x[0] - i - 1] - 1) % 8
        else:
            break
        i += 1
    # print(d_)
    d = d_


result = 0
if wheels[1][(d[1] + 2) % 8] == 1:
    result += 1
if wheels[2][(d[2] + 2) % 8] == 1:
    result += 2
if wheels[3][(d[3] + 2) % 8] == 1:
    result += 4
if wheels[4][(d[4] + 2) % 8] == 1:
    result += 8
print(result)