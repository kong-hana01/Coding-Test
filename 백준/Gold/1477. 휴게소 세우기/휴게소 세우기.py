# https://www.acmicpc.net/problem/1477
# 접근 방법
# 이진탐색을 활용해 문제를 해결한다.
n, m, l = map(int, input().split())
arr = [0] + list(map(int, input().split())) + [l]
arr.sort()

start = 1
end = l
result = l
while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for i in range(1, n+2):
        dist = arr[i] - arr[i-1]
        while dist > mid and cnt <= m:
            dist -= mid
            cnt += 1
    
    if cnt <= m:
        result = min(result, mid)
        end = mid - 1
    
    else:
        start = mid + 1

print(result)