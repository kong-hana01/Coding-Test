# https://www.acmicpc.net/problem/2109
# 접근 방법
# 0. 주어진 강연정보를 각 대학별 날짜를 기준으로 오름차순 정렬하고, 강연 페이를 기준으로 하는 최소힙을 초기화한다.
# 1. 강연정보를 하나씩 탐색하며 최소힙의 길이보다 현재 탐색중인 날짜가 크다면 이를 최소힙에 삽인한다.
# 2. 만약 최소힙의 길이가 현재 탐색중인 날짜보다 같다면 최소힙의 0번째 인덱스와 현재 탐색중인 강연의 급여를 비교해 더 큰 값을 삽입하고 작은 값은 최소힙에 넣지 않거나 뺀다.
# 모든 탐색이 끝난 뒤, 최소힙을 모두 합해 값을 출력한다.
import sys, heapq
input = sys.stdin.readline
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key=lambda x: x[1])
min_heap = []
for pay, day in array:
    if day > len(min_heap):
        heapq.heappush(min_heap, pay)
    else:
        if min_heap[0] < pay:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, pay)
total_pay = sum(min_heap)
print(total_pay)