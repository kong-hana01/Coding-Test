# https://www.acmicpc.net/problem/2036
# 접근 방법
# 양수와 음수를 분할해 힙정렬을 한 뒤, 뒤에서부터 두 값을 곱해 점수를 합산한다.
import sys, heapq
input = sys.stdin.readline
n = int(input())
seq = [int(input()) for _ in range(n)]
min_h = []
max_h = []
for x in seq:
    if x <= 0:
        heapq.heappush(min_h, x)
    else:
        heapq.heappush(max_h, -x)

result = 0
while max_h:
    if len(max_h) >= 2:
        x1 = -heapq.heappop(max_h)
        if max_h[0] != -1:
            x2 = -heapq.heappop(max_h)
        else:
            x2 = 1
        result += x1 * x2
    else:
        result += -heapq.heappop(max_h)

while min_h:
    if len(min_h) >= 2:
        x1 = heapq.heappop(min_h)
        x2 = heapq.heappop(min_h)
        result += x1 * x2
    else:
        result += heapq.heappop(min_h)

print(result)