# https://www.acmicpc.net/problem/3745
# 접근 방법
# 가장 긴 부분 수열을 nlogn으로 구현해 가장 긴 오름세를 찾는다.
import sys
input = sys.stdin.readline
while True:
    n = input()
    if not n:
        break
    n = int(n)
    array = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[0] = array[0]
    length = 1
    for x in array[1:]:
        start = 0
        end = length - 1
        index = 0
        while start <= end:
            mid = (start + end) // 2
            
            if dp[mid] < x:
                start = mid + 1
                index = max(index, mid+1)
            
            else:
                end = mid - 1
                
        length = max(index+1, length)
        dp[index] = x

    print(length)