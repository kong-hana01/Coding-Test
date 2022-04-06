# https://www.acmicpc.net/problem/1182
# 접근 방법
# 모든 부분수열을 탐색하여 부분수열이 S가 되는 경우의 수를 모두 구해 출력한다.
n, s = map(int, input().split())
arr = list(map(int,input().split()))
count = 0
for i in range(n):
    total_sum = arr[i]
    count += 0 if total_sum != s else 1
    for j in range(i+1, n):
        total_sum += arr[j]
        count += 0 if total_sum != s else 1
print(count)