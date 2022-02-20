# https://www.acmicpc.net/problem/2110
# 접근 방법
# 집 간의 거리를 기준으로 이진탐색을 진행한 뒤, 그 인접한 두 공유기 사이의 최대 거리를 출력한다.
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
start = 0
end = 1000000000
max_distance = 0
while start <= end:
    mid = (start+end) // 2
    min_distance = end
    last = arr[0]
    count = 1
    for i in range(n):
        if arr[i] - last >= mid:
            min_distance = min(min_distance, arr[i] - last)
            count += 1
            last = arr[i]
    
    if count >= c:
        max_distance = max(min_distance, max_distance)
        start = mid + 1
    
    else:
        end = mid - 1
    
print(max_distance)