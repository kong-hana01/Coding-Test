# https://www.acmicpc.net/problem/1374
# 접근 방법
# 강의 시작 시간을 기준으로 오름차순 정렬한 뒤, 이를 하나씩 탐색한다.
# 강의 끝나는 시간을 기준으로 최소힙을 구성해 시작 시간보다 일찍 끝나는 강의는 모두 뺀다.
# 매번 강의를 탐색할 때마다 최소힙의 개수를 구해 이의 최대값을 구한 뒤, 이를 출력한다.
import heapq, sys
input = sys.stdin.readline
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key = lambda x: x[1])
min_h = []
count = 0
for x in array:
    while min_h and min_h[0] <= x[1]:
        heapq.heappop(min_h)
    heapq.heappush(min_h, x[2])
    count = max(count, len(min_h))
print(count)