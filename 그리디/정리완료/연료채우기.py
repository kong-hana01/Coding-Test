# https://www.acmicpc.net/problem/1826
# 접근 방법
# 현재 저장되어있는 연료를 기준으로 최대 갈 수 있는 거리까지의 주유소의 연료양을 최대 힙에 삽입하여 주유소를 탐색하며 주유소에서 멈춰야하는 최소 횟수를 출력한다.
import heapq
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())
array.sort(key=lambda x: x[0])
h = []
count = 0
for distance, fuel in array:
    while distance > p and h:
        p += -heapq.heappop(h)
        count += 1
    if distance > p:
        break
    heapq.heappush(h, -fuel)

while l > p and h:
    p += -heapq.heappop(h)
    count += 1

if l > p:
    print(-1)
else:
    print(count)