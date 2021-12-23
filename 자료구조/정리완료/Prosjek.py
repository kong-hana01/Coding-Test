# https://www.acmicpc.net/problem/15577
# 접근 방법
# 작은 숫자 두개를 선택해 두 숫자의 평균을 저장한 뒤, 이를 우선순위 큐에 저장한다.
# 출력은 소수점 6자리까지 출력한다.
import heapq
n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))

for _ in range(n-1):
    x1 = heapq.heappop(h)
    x2 = heapq.heappop(h)
    heapq.heappush(h, (x1+x2) / 2)
print('{:.6f}'.format(h[0]))