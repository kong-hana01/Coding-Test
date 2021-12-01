# https://www.acmicpc.net/problem/12018
# 접근 방법
# 각 과목별로 신청한 사람의 마일리지를 내림차순으로 정렬한 뒤, l번째 점수가 몇 점인지 확인해, l번째 점수 + 1을 우선순위 큐에 저장한다.
# 모든 과목을 우선순위 큐에 저장한 뒤, 마일리지를 최대한 활용해 들을 수 있는 과목이 몇 개인지 센다.
import heapq
n, m = map(int, input().split())
subject = [[] for _ in range(n)]
h = []
for _ in range(n):
    p, l = map(int, input().split())
    mileage = sorted(list(map(int, input().split())), reverse = True)
    if l > p:
        heapq.heappush(h, 1)
    else:
        heapq.heappush(h, mileage[l-1])
count = 0
while h and m - h[0] >= 0:
    x = heapq.heappop(h)
    m -= x
    count += 1
print(count)