# https://www.acmicpc.net/problem/2374
# 접근 방법
# 주어진 자연수를 하나씩 탐색하며 연속된 같은 수를 하나의 집합으로 보고 해당 숫자를 첫번째 값, 집합의 범위를 리스트로 가지는 리스트로 만들어 이를 최소 힙에 저장한다.
# 힙을 하나씩 탐색하며 범위 앞, 뒤에 있는 값 중 작은 값을 기준으로 수를 연산을 진행한 뒤, 해당 범위를 늘려준 뒤, 다시 힙에 저장한다.
# 힙을 탐색할 때 만약 힙에 저장된 범위 밖에 있는 값과 현재 저장된 값이 같다면 이는 pop한 뒤, 힙을 다시 탐색한다.
# 모든 힙의 범위가 0부터 n-1까지로 설정된다면 탐색을 종료하고 연산 횟수를 출력한다.
import heapq
n = int(input())
arr = [int(input()) for _ in range(n)]

h = []
start = 0
now_value = arr[0]
for i in range(1, n):
    if now_value != arr[i]:
        heapq.heappush(h, [now_value, start, i-1])
        now_value = arr[i]
        start = i

if now_value == arr[n-1]:
    heapq.heappush(h, [now_value, start, n-1])

union = [[] for _ in range(n)]
for v, s, e in h:
    for i in range(s, e+1):
        union[i] = [s, e]

count = 0
while h[0][1] != 0 or h[0][2] != n-1 :
    value, start, end = heapq.heappop(h)
    if (start > 0 and arr[start - 1] == arr[start]) or (end < n - 1 and arr[end+1] == arr[end]):
        continue
    # 범위 설정
    if start > 0 and end < n - 1:
        if arr[start - 1] < arr[end + 1]:
            min_value = arr[start - 1]
            new_start, new_end = union[start - 1][0], end
        elif arr[start - 1] > arr[end + 1]:
            min_value = arr[end + 1]
            new_start, new_end = start, union[end + 1][1]
        else:
            min_value = arr[start - 1]
            new_start = union[start - 1][0]
            new_end = union[end + 1][1]

    else:
        if start > 0:
            min_value = arr[start - 1]
            new_start, new_end = union[start - 1][0], end
        else:
            min_value = arr[end + 1]
            new_start, new_end = start, union[end + 1][1]
    count += min_value - value
    value = min_value

    for i in range(start, end+1):
        arr[i] = value
    for i in range(new_start, new_end+1):
        union[i] = [new_start, new_end]

    heapq.heappush(h, [value, new_start, new_end])


print(count)