# https://www.acmicpc.net/problem/14659
# 접근 방법
# 값을 하나씩 탐색할 때마다 자기 자신이 나온 위치보다 높은 위치의 봉우리가 나올 떄까지의 봉우리 개수를 갱신한다.
# 탐색이 끝난 뒤, 가장 긴 길이를 출력한다.
n = int(input())
arr = list(map(int, input().split()))
now = 0
max_length = 0
count = 0
for i in range(1, n):
    if arr[now] < arr[i]:
        max_length =  max(count, max_length)
        now = i
        count = 0
        continue
    count += 1

print(max(max_length, count))
