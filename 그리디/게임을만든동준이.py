# https://www.acmicpc.net/problem/2847
# 접근방법
# 이전 값이 다음 값보다 작도록 값을 빼주면 된다.
n = int(input())
arr = [int(input()) for _ in range(n)]
arr = arr[::-1]
now_score = arr[0]
total_score = 0
for i in range(1, n):
    if now_score <= arr[i]:
        total_score += arr[i] - now_score + 1
        arr[i] = now_score - 1
        
    now_score = arr[i]
    
print(total_score)