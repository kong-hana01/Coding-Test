# https://www.acmicpc.net/problem/19941
# 0. 햄버거와 사람에 대한 정보를 차례로 탐색한다.
# 1. 햄버거가 나올 경우 해당 위치를 중심으로 하는 minheapH에 저장한다.
# 2. 사람이 나올 경우에는 해당 위치를 중심으로 하는 minheapP에 저장한다.
# 3. minheapP를 기준으로 값을 하나씩 빼며, k개 이내에 위치한 minheapH에 저장된 햄버거를 하나씩 세고 빼주며 햄버거를 먹을 수 있는 사람의 수를 증가한다.
# 3-1. 단, 햄버거의 위치가 더 낮은데, 사람과의 거리가 k 이상이라면 minheapH에서 값을 빼주고, 사람의 위치가 더 낮은데 햄버거와의 거리가 k 이상이라면 minheapP에서 값을 빼준다.
import heapq

n, k = map(int, input().split())
arr = input()
minheapH = []
minheapP = []
for i in range(n):
    if arr[i] == 'H':
        heapq.heappush(minheapH, i)
    else:
        heapq.heappush(minheapP, i)

count = 0
while minheapP:
    x = heapq.heappop(minheapP)
    while minheapH:
        if minheapH[0] - x > k:
            break
        y = heapq.heappop(minheapH)
        if abs(x - y) <= k:
            count += 1
            break
print(count)