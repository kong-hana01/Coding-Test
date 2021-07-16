# https://www.acmicpc.net/problem/14890
# 접근방법
# 주어진 높이를 하나씩 탐색하며 주어진 조건에 따라 길을 만들 수 있는지 확인한다.
# 조건 1. 진행 방향에 있는 높이가 같은 경우는 다음 높이를 탐색한다.
# 조건 2. 높이가 2이상 차이날 경우 더이상 확인하지 않고 넘어간다.
# 조건 3-1. 높이가 1만큼 차이가 나고, 현재 저장한 높이가 더 높은 경우에는 진행 방향에 있는 높이가 L만큼 연속되어있는지 확인하고 있다면 계속 탐색한다.
# 조건 3-2. 높이가 1만큼 차이가 나고, 현재 저장한 높이가 더 낮은 경우에는 해당 높이가 L만큼 연속되어있는지 확인하고 있다면 계속 탐색한다.
# 위의 과정을 반복하고 지나갈 수 있는 길의 개수를 출력한다.

n, l = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n):
    count = 0
    count_now = 0
    count_next = 0
    standard_height = map_[i][0]
    for j in range(n): # 행 탐색
        
        if standard_height == map_[i][j] and count_next == 0:
            count_now += 1
            count += 1
            continue
        
        elif abs(standard_height - map_[i][j]) > 1:
            break

        elif abs(standard_height - map_[i][j]) == 1:
            if standard_height < map_[i][j] and count_next == 0:
                if count_now >= l: 
                    standard_height = map_[i][j]
                    count_now = 1
                    count += 1
                else:
                    break

            else:
                count_next += 1
                if count_next >= l:
                    standard_height = map_[i][j]
                    count += count_next
                    count_now, count_next = 0, 0
        else:
            break

    if count == n:
        result += 1
        # print(f'행 탐색: {i+1}')
        

for i in range(n):
    count = 0
    count_now = 0
    count_next = 0
    standard_height = map_[0][i]
    for j in range(n): # 열 탐색

        if standard_height == map_[j][i] and count_next == 0:
            count_now += 1
            count += 1
            pass
        elif abs(standard_height - map_[j][i]) > 1:
            break
        elif abs(standard_height - map_[j][i]) == 1:
            if standard_height < map_[j][i]:
                if count_now >= l and count_next == 0: 
                    standard_height = map_[j][i]
                    count_now = 1
                    count += 1
                else:
                    break
            else:
                count_next += 1
                if count_next >= l:
                    standard_height = map_[j][i]
                    count += count_next
                    count_now, count_next = 0, 0
        else:
            break
        

        # if i == 0:
        #     print(j)
        #     print(f'standard: {standard_height}')
        #     print(f'count_now: {count_now}, count_next: {count_next}')
        #     print(f'- {map_[j][i]}')

    if count == n:
        result += 1
        # print(f'열 탐색: {i+1}')
print(result)
