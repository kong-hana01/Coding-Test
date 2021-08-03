# https://www.acmicpc.net/problem/15922
# 접근 방법
# 첫 x와 y를 각각 start, end 변수에 저장한다.
# 이후 n개의 선분을 탐색하며 end보다 xi가 작은 경우 end의 길이를 yi로 늘린다.
# 만약 end가 xi보다 작다면 end - start를 result에 누적합한 뒤, start와 end를 xi와 yi로 초기화한다.
# 모든 탐색이 끝난 뒤, end - start를 result에 누적합한 뒤, 이를 출력한다.
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
start, end = array[0][0], array[0][1]
result = 0
for x, y in array:
    if x <= end:
        end = max(y, end)
    else:
        result += end - start
        start, end = x, y
result += end - start
print(result)