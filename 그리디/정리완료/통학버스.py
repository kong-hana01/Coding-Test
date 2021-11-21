# https://www.acmicpc.net/problem/2513
# 접근 방법
# 학교의 위치에서 각 아파트 단지에 대한 거리를 기준으로 하는 최대힙을 활용해 문제를 해결한다.
import heapq
n, k, s = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
h1, h2 = [], []
for x in array:
    if x[0] < s:
        heapq.heappush(h1, [-(s-x[0]), x[1]]) # 학교보다 낮은 위치
    else:
        heapq.heappush(h2, [-(x[0]-s), x[1]]) # 학교보다 높은 위치

result = 0
count = 0
distance = 0
while h1:
    dist, c = heapq.heappop(h1)
    if not distance:
        distance = -dist * 2
        result += distance

    if count + c > k:
        c -= k - count
        count = 0
        distance = 0
        heapq.heappush(h1, [dist, c])

    else:
        count += c
        

count = 0
distance = 0
while h2:
    dist, c = heapq.heappop(h2)
    if not distance:
        distance = -dist * 2
        result += distance

    if count + c > k:
        c -= k - count
        count = 0
        distance = 0
        heapq.heappush(h2, [dist, c])

    else:
        count += c

print(result)