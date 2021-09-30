import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
INF = int(1e9)
dp = [INF for _ in range(n)]

result = 0
for x in array:
    start = 0 
    end = result
    count = 0
    while start <= end:
        mid = (start + end) // 2
        
        if dp[mid] >= x:
            end = mid - 1
        elif dp[mid] < x:
            start = mid + 1
            count = max(mid + 1,count)
        
        result = max(result, count+1)
    dp[count] = x

print(result)        