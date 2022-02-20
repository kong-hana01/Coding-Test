# https://www.acmicpc.net/problem/12931
# 접근 방법
# B 수열의 원소가 홀수인 경우 숫자를 하나씩 빼주고, 모든 원소가 짝수라면 2를 나눠준다.

n = int(input())
arr = list(map(int, input().split()))
count = 0
while True:
    zero_count = 0
    for i in range(n):
        if arr[i] % 2:
            arr[i] -= 1
            count += 1
            
        if arr[i] == 0:
            zero_count += 1
    
    if zero_count == n:
        print(count)
        break
    
    else:
        count += 1
        for i in range(n):
            arr[i] //= 2