# 접근 방법
# 선분을 입력받은 뒤 선분의 왼쪽 좌표를 기준으로 오름차순 정렬하고 첫번째 인덱스에 있는 오른쪽 좌표를 min heap에 저장한다.
# 이후 선분을 하나씩 탐색하며 탐색중인 선분의 왼쪽 좌표와 min heap에 저장된 오른쪽 좌표를 비교해 왼쪽좌표보다 낮은거는 모두 삭제한다.
# 삭제가 끝나면 현재 탐색중인 선분의 오른쪽 좌표를 min heap에 삽입한 뒤 결과 값에 결과값과 길이 중 더 높은 숫자를 저장한다.
# 모든 탐색이 끝난 뒤 결과값을 출력한다.
import sys, heapq
input = sys.stdin.readline
n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]
array.sort(key=lambda x:x[0])
min_heap = []
heapq.heappush(min_heap, array[0][1])
result = 1
for x in array[1:]:
    while min_heap and min_heap[0] <= x[0]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, x[1])
    result = max(result, len(min_heap))

print(result)