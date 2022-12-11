# https://www.acmicpc.net/problem/16678
# 접근 방법
# 국회의원의 명예점수를 정렬한 뒤, 이전 값보다 1씩 작게 만드는데 소요되는 비용을 계산해 처리한다.
# 단, 동일한 점수인 경우에는 모든 국회의원을 모독하는 경우가 1번이라는 점을 고려하여 처리한다.
import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
result = arr[0] - 1
arr[0] = 1
for i in range(1, n):
    if arr[i-1] + 1 < arr[i]:
        result += arr[i] - (arr[i-1] + 1)
        arr[i] = arr[i-1] + 1
print(result)