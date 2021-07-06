# https://www.acmicpc.net/problem/19598
# 접근 방법
# 시작 시간을 기준으로 하는 최소 힙(start_heap)을 만들어 회의 시간을 입력받는다.
# start_heap에서 원소를 하나씩 빼고 이를 끝나는 시간을 기준으로 하는 최소힙(end_heap)의 0 인덱스의 요소와 비교한 뒤, 이 시간보다 클 경우 end_heap의 원소를 빼고 해당 값을 삽입한다.
# 삭제와 삽입을 반복할 떄마다 end_heap의 길이의 최댓값을 저장한뒤, 출력한다.
import sys, heapq
n = int(sys.stdin.readline()) # 회의실 개수 입력
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 회의 시간 리스트 입력
start_heap = [] # 시작 시간을 기준으로 하는 최소힙
end_heap = [] # 끝나는 시간을 기준으로 하는 최소힙

for x in array:
    heapq.heappush(start_heap, [x[0], x[1]]) # start_heap 값 푸쉬

x = heapq.heappop(start_heap)
heapq.heappush(end_heap, [x[1], x[0]]) # end_heap 값 초기화

result = 1 # 결과 값 초기화
while start_heap:
    x = heapq.heappop(start_heap) # 회의 시간 탐색
    if end_heap[0][0] <= x[0]:
        heapq.heappop(end_heap)
    heapq.heappush(end_heap, [x[1], x[0]])
    result = max(result, len(end_heap))
print(result)