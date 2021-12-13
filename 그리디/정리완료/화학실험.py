# https://www.acmicpc.net/problem/20311
# 접근 방법
# 0. 각 시험관의 개수를 최대 힙에 저장한 뒤, 이를 하나씩 빼내어주며 배열(result)에 저장한다. 
# 1. 이때 값을 하나씩 빼내어 줄 때마다 다른 리스트(temp)에 저장하고, 만일 리스트에 값이 존재하는 경우 해당 값을 빼내어 최대 힙에 다시 저장한다.
# 2. 최대 힙에 값이 없거나, result에 값이 연속되는 경우 동작을 중단한다.
# 3. 만일 result에 있는 값이 연속되는 경우 -1을 출력한다.
# 4. 3번에 해당되지 않는다면 배열의 원소를 출력조건에 맞게 출력한다.
import sys, heapq
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
maxH = []
for i in range(k):
    heapq.heappush(maxH, [-arr[i], i])

flag = True
result = []
temp = []
while maxH:
    
    value, index = heapq.heappop(maxH)
    result.append(index+1)
    if len(result) >= 2 and result[-1] == result[-2]:
        flag = False
        break

    if temp:
        x = temp.pop()
        if x[0] < 0:
            heapq.heappush(maxH, x)    
    

    temp.append([value + 1, index])


if not flag or temp[0][0] <= -1:
    print(-1)

else:
    for x in result:
        print(x, end = ' ')
