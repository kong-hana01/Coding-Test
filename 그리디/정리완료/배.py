# 접근 방법
# 0. 주어진 박스의 크기와 크레인의 무게를 내림차순으로 정렬한다.
# 1. min heap을 통해 각 크레인 당 박스를 옮긴 횟수를 저장하여 옮긴 박스의 갯수를 기준으로 만든다.
# 2. 크레인의 무게를 기준으로 한 리스트의 인덱스를 기준으로 현재 박스를 옮길 수 있으면 해당 크레인의 정보를 min heap에 삽입한다.
# 3. 박스를 옮긴 횟수를 매번 갱신해주며 모든 탐색이 끝났을 때 박스를 옮긴 최대값을 출력한다.
import heapq
n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
crane.sort(reverse=True)
box.sort(reverse=True)

i = 0
min_heap = []
result = 0
for x in box:
    while n > i and crane[i] >= x:
        heapq.heappush(min_heap, [0, crane[i]])
        i += 1
    if not min_heap:
        result = -1
        break
    count, c = heapq.heappop(min_heap)
    count += 1
    heapq.heappush(min_heap, [count, c])


while min_heap:
    x = heapq.heappop(min_heap)
    result = max(result, x[0])
print(result)