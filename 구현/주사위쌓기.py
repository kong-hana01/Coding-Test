# https://www.acmicpc.net/problem/2116
# 접근 방법
# 첫 주사위의 윗면을 어떤 걸로 할지를 1부터 6까지 반복하고, 이에 따른 다른 주사위들의 윗면, 아랫면을 정하고, 나머지 면 중 가장 높은 눈을 누적해 모든 주사위에 대해 최댓값을 구한 뒤 이를 출력한다.


n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
top_down_dict = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
result_total_num = 0
for i in range(6):
    top_idx = i
    bottom_idx = top_down_dict[top_idx]
    temp_total_num = max([dices[0][idx] for idx in range(6) if idx not in [top_idx, bottom_idx]])
    for j in range(1, n):
        for k in range(6):
            if dices[j-1][top_idx] == dices[j][k]:
                bottom_idx = k
                break
        top_idx = top_down_dict[bottom_idx]
        max_num = max([dices[j][idx] for idx in range(6) if idx not in [top_idx, bottom_idx]])
        temp_total_num += max_num
        
    result_total_num = max(result_total_num, temp_total_num)
print(result_total_num)