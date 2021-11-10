# https://www.acmicpc.net/problem/2457
# 접근 방법
# 0. 각 꽃들에 대해 1월 1일부터 각 날짜까지의 일자를 기준으로 수정한다. [꽃이 피는 일, 꽃이 지는 일]
# 1. 이후 꽃의 처음 값을 기준으로 오름차순 정렬한다. 
# 2. 처음 값은 3월 1일 이전에 피는 꽃 중 가장 늦게까지 피는 꽃의 지는 날짜를 기준으로 설정한다.
# 3-1. 매번 꽃을 탐색할 때마다 현재 기준 값보다 일찍 꽃이 피는 꽃들 가운데 가장 늦게 꽃이 지는 날짜를 기준으로 값을 갱신한다.
# 3-2. 꽃을 탐색하는데 현재 기준 값보다 일찍 꽃이 피는 것이 없다면 탐색을 중단하고 0을 출력한다.
# 4. 모든 탐색을 끝낸 뒤, 이상이 없다면 갱신된 값을 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_month = [0 for _ in range(13)]
for i in range(1, 13):
    sum_month[i] = sum_month[i-1] + month[i]
flowers = [list(map(int, input().split())) for _ in range(n)]
array = []
for x in flowers:
    array.append([sum_month[x[0]-1] + x[1], sum_month[x[2]-1] + x[3]])
array.sort(key = lambda x:x[0])
start = sum_month[2] + 1
end = sum_month[10] + 30
count = 0

flag = True
max_length = 0
for x in array:
    if x[0] <= start and x[1] > start:
        flag = False
        max_length = max(max_length, x[1])
        if max_length > end:
            count += 1
            break

    elif max_length < x[0]:
        break

    elif x[0] > start:
        count += 1
        if flag: 
            break   
        flag = True
        start = max_length
        if max_length < x[1]:
            max_length = x[1]
            flag = False
            if max_length > end:
                count += 1
                break

if flag or max_length <= end:
    print(0)
else:
    print(count)
        
