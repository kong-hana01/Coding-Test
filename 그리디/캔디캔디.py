# https://www.acmicpc.net/problem/2878
# 접근 방법
# 못받은 사탕의 개수가 많아질수록 더 많은 분노가 생기기때문에 이를 최소화하기 위해선 못받은 사탕의 개수를 최소화하는 것이 중요하다.
# 따라서 모든 사람들을 대상으로 못 받는 사탕의 최대 개수를 기준으로 이진탐색을 진행하고 나머지 값에 대해선 최대힙에서 값을 뺀 뒤, 분노의 합을 구한다.
import sys, heapq
input = sys.stdin.readline

m, n = map(int, input().split())
array = [int(input()) for _ in range(n)]
max_value = max(array)

start = 0
end = max_value
result = max_value
while start <= end:
    mid = (start+end)//2
    count = 0
    for x in array:
        count += max(x - mid, 0)
    if count <= m:
        result = min(result, mid)
        end = mid - 1
    
    else:
        start = mid + 1

q = []
for i in range(n):
    if array[i] > result:
        m -= array[i] - result
        array[i] = result
    heapq.heappush(q, -array[i])

while m > 0:
    x = -heapq.heappop(q)
    heapq.heappush(q, -(x-1))
    m -= 1

print(sum([x ** 2 for x in q]) % 2**64)