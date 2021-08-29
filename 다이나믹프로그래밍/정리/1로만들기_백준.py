# https://www.acmicpc.net/problem/1463
# 접근방법
# dp 테이블을 x+1개만큼 초기화한다.(인덱스: 연산한 값 x, 값: 연산 횟수)
# 이후 3가지 경우의 수를 인덱스로 하는 dp테이블의 값이 없을 경우 연산을 거친 것을 queue에 삽입하고 dp 테이블에 연산횟수를 입력한다.
# x가 1이 될 때 연산횟수를 출력한다.
from collections import deque
x = int(input())
queue = deque([])
d = [0] * (x+1)
d[x] = 1
while not d[1]:
    
    if x % 3 == 0 and not d[x//3]:
        d[x//3] = d[x] + 1
        queue.append(x//3)
    if x % 2 == 0 and not d[x//2]:
        d[x//2] = d[x] + 1
        queue.append(x//2)
    if not d[x-1]:
        d[x-1] = d[x] + 1
        queue.append(x-1)
    x = queue.popleft()

print(d[1] - 1)