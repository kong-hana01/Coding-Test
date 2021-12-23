# https://www.acmicpc.net/problem/23757
# 접근 방법
# 최대힙을 통해 개수를 갱신해주면 가장 앞에 있는 선물 상자의 선물 개수를 매번 빼준다.
# 이때 음수가 나오면 이를 종료하고 0을 출력한다.
import heapq
n, m = map(int, input().split())
c = []
for x in list(map(int, input().split())):
    heapq.heappush(c, -x)
w = list(map(int, input().split()))

is_neg = False
for i in w:
    x = -heapq.heappop(c)
    if x - i < 0:
        is_neg = True
        break
    heapq.heappush(c, -(x-i))

if is_neg:
    print(0)
else:
    print(1)