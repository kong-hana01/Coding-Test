# https://www.acmicpc.net/problem/1546
n = int(input())
arr = list(map(int, input().split()))
print(arr)
max_score = max(arr)
result = sum(arr) / max(arr) * 100 / len(arr)
print(result)