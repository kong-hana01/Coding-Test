# https://www.acmicpc.net/problem/9237
# 접근 방법
# 내림차순으로 정렬해 시간을 계산한다.
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
result = 0
for i in range(n):
    result = max(result, arr[i] + i + 1)
print(result + 1)