# https://www.acmicpc.net/problem/2024
# 접근 방법 -> 추후 재시도
# 주어진 선분을 왼쪽 좌표를 기준으로 오름차순 정렬한 뒤, 선분을 하나씩 탐색한다.
# 선분을 하나씩 탐색하며 현재 스텍에 저장되어있는 선분들과 비교해 특정 조건에 해당하면 선분을 삽입하고 삭제한다.
# 1. 스텍에 값이 없는 경우 선분을 삽입한다.
# 2. 현재 탐색 중인 선분의 오른쪽 좌표가 스텍 마지막에 있는 선분의 오른쪽 좌표보다 클 경우 선분을 삽입한다.
# 3-1. 현재 탐색 중인 선분의 왼쪽 좌표가 스텍 마지막 이전 인덱스의 오른쪽 좌표보다 큰 경우 스텍 마지막에 있는 선분을 삭제한다.
# 3-2. 단, 왼쪽 선분의 좌표가 0이상이고, 마지막에 있는 선분의 오른쪽 좌표가 현재 탐색중인 선분의 오른쪽 좌표보다 작다면 스텍에 있는 모든 좌표를 삭제한 뒤 현재 탐색중인 선분을 저장하고, 그렇지 않다면 현재 선분을 삽입하지 않는다.
# 모든 탐색을 마친 뒤, 스텍에 있는 개수를 출력한다.

m = int(input())
array = []
while True:
    l, r = map(int, input().split())
    if l == r == 0:
        break
    if r <= 0:
        continue
    array.append([l, r])
array.sort(key=lambda x: (x[0], x[1]))
stack = []
for x1, x2 in array:
    while (len(stack) >= 2 and stack[-2][1] >= x1 >= stack[-1][1]) or (stack and x1 <= 0 and x2 >= stack[-1][1]):
        stack.pop()
    if stack and stack[-1][1] >= x2:
        continue
    stack.append([x1, x2])
if stack[0][0] <= 0 and stack[-1][1] == m:
    print(len(stack))
else:
    print(0)