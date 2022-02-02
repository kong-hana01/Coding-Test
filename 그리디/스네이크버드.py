# https://www.acmicpc.net/problem/16435
# 접근 방법
# 과일의 높이를 정렬한 뒤, 하나씩 탐색해 버드의 최대 길이를 출력한다.
n, l = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
for h in heights:
    if l < h:
        break
    l += 1
print(l)