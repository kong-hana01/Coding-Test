# https://www.acmicpc.net/problem/2594
# 접근 방법
# 0. 주어진 숫자를 분단위로 바꾸어 저장한다.
# 1. 놀이기구 시작시간을 기준으로 값을 정렬한 뒤, 값을 하나씩 탐색하며 쉬는 시간을 계산하여 가장 긴 쉬는 시간을 출력한다.
n = int(input())
arr = [list(map(lambda x: int(x[:2]) * 60 + int(x[2:]), input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
result = max(0, arr[0][0] - 610)
e = arr[0][1]
for x in arr:
    if x[0] - 10 > e + 10:
        result = max(x[0] - (e + 20), result)
    e = max(x[1], e)
result = max(60*22 - (e + 10), result)
print(result)