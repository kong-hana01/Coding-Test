# https://www.acmicpc.net/problem/2012
# 접근방법
# 최소힙에 값을 모두 저장한 뒤, 하나씩 빼내어, 등수를 증가시키며 등수와 뺀 값의 차이를 합계에 저장한다.
# 모든 값을 빼낸 뒤, 합계를 출력한다.
import sys, heapq
input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))

rank = 1
result = 0
while h:
    x = heapq.heappop(h)
    result += abs(rank - x)
    rank += 1
print(result)