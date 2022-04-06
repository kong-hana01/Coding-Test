# https://www.acmicpc.net/problem/2792
# 접근 방법
# 이진탐색을 통해 아이들에게 보석을 나눠주고 질투심이 최소가 되도록 보석을 나눠준다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
jewels = [int(input()) for _ in range(m)]
start = 1
end = sum(jewels)
result = end
while start <= end:
    mid = (start+end) // 2
    count = 0
    for jewel in jewels:
        count += (jewel // mid) + (1 if jewel % mid else 0)
    
    if count <= n:
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1
    
print(result)
