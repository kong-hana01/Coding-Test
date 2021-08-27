# https://www.acmicpc.net/problem/13164
# 접근 방법
# 티셔츠를 만드는 비용을 기준으로 이진탐색을 진행한다.
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = array[-1] - array[0]
cost = end
result = 0
while start <= end:
    mid = (start+end) // 2
    count = 1
    min_height = array[0]
    total = 0
    for i in range(1, n):
        h = array[i]
        if h - min_height > mid:
            total += array[i-1] - min_height
            min_height = h
            count += 1
    total += array[-1] - min_height

    if count > k:
        start = mid + 1
    
    elif count < k:
        end = mid - 1
    
    else:
        end = mid - 1
        if cost > mid:
            cost = mid
            result = total

print(result)