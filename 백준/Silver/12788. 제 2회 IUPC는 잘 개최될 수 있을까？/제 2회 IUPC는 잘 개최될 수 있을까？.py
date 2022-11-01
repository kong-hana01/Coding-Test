# https://www.acmicpc.net/problem/12788
# 접근 방법
# 그리디 알고리즘을 통해 문제를 해결한다.
import heapq
n = int(input())
m, k = map(int, input().split())
h = []
for x in map(int, input().split()):
    heapq.heappush(h, -x)
result = 0
cntOfNeed = m*k
while cntOfNeed>0 and h:
    cntOfNeed += heapq.heappop(h)
    result += 1

if cntOfNeed <= 0:
    print(result)
else:
    print('STRESS')