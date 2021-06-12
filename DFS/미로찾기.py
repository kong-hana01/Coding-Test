n, m = 5, 6
map_ = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

# 처음 시작할 때의 위치는 0, 0
map_[0][0] = 0
count = 0
count_list = []
step_list = [[0, 0]]

# dfs
# 1번 : 현재 위치에서 움직일 수 있는 경우의 수를 스택에 쌓는다.
# 2번 : 하나씩 꺼내며 그 위치로 이동 후 스텝은 +1, 그 곳에서의 경우의 수는 스택에 쌓는 과정을 반복한다.
# 3번 : 이를 반복하며 방문한 위치는 0으로 초기화한다.
# 4번 : n, m으로 도달한다면 해당 장소에 이동하기위해 움직인 횟수를 리턴한다.

def dfs(n, m, count):
    count += 1
    while step_list != []:
        no_step = 0
        col, row = step_list[-1]
        step_list.pop() 
        for dcol, drow in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            new_col, new_row = dcol+col, drow+row
            if 0 <= new_col <= n-1 and 0 <= new_row <= m-1 and map_[new_col][new_row] == 1:
                map_[new_col][new_row] = 0
                step_list.append([new_col, new_row])
                print(new_col, new_row, '방문')
                dfs(n, m, count)
                if new_col == n-1 and new_row == m-1:
                    count += 1
                    count_list.append(count)

        map_[col][row] = 1
    
        #     else:
        #         no_step += 1

        # if no_step == 4:
        #     return 

dfs(n, m, count)
print(min(count_list))