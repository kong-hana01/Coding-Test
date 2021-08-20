# https://www.acmicpc.net/problem/17822
# 접근 방법
# 0. 원판과 원판에 적힌 수를 이중 리스트로 입력받는다. 단, 원판을 입력받을 때 인덱스가 1부터 시작하도록 입력받는다.
# 1. 원판을 회전시키는 함수를 만든다.
# 1-1. 원판 내에 있는 숫자는 나머지 연산자를 활용해 인덱스를 이동한다.
# 2. 인접한 숫자를 제거하는 함수를 만든다.
# 2-1. 원판을 하나씩 탐색하며 원판 내에 있는 인접한 숫자는 나머지 연산자를 활용해 구한다.
# 2-2. 원판간의 인접한 숫자는 주어진 원판 개수 범위 내에 있는지 확인한 뒤, 인접한 숫자를 구한다.
# 2-3. 동일한 인접한 숫자가 있다면 인접한 숫자의 인덱스를 저장한다.
# 2-4. 인접한 숫자가 없는 경우엔 평균을 구한 뒤, 다시 한번 원판을 하나씩 탐색하며 값을 1씩 더하거나 뺀다.
# 3. 1번과 2번을 t번만큼 반복한 뒤, 원판에 남아있는 숫자를 출력한다.
def Rotate(array):
    # 1. 원판을 회전시키는 함수
    x, d, k = map(int, sys.stdin.readline().split())
    
    if d == 0: # 시계 방향
        for i in range(x, n+1, x):
            array[i] = [array[i][(j-k)%m] for j in range(m)]

    else: # 반시계 방향
        for i in range(x, n+1, x):
            array[i] = [array[i][(j+k)%m] for j in range(m)]

def Find_adjacent_number(array):
    # 2. 인접한 동일한 숫자를 찾는 함수
    adjacent_same_number = []
    total = 0
    count = 0
    for i in range(1, n+1):
        for j in range(m):
            if array[i][j]:
                # 원판 내 인접한 숫자 찾기
                if array[i][j] == array[i][(j+1)%m]:
                    adjacent_same_number.append([i, (j+1)%m])
                if array[i][j] == array[i][(j-1)%m]:
                    adjacent_same_number.append([i, (j-1)%m])
                
                # 원판 간의 인접한 숫자 찾기
                if 1 <= i - 1 and array[i][j] == array[i-1][j]:
                    adjacent_same_number.append([i-1, j])
                if i + 1 <= n and array[i][j] == array[i+1][j]:
                    adjacent_same_number.append([i+1, j])
                
                total += array[i][j]
                count += 1
    
    if adjacent_same_number: # 인접한 숫자가 있다면
        for i, j in adjacent_same_number:
            array[i][j] = 0

    else: # 인접한 숫자가 없다면 평균 값으로 1을 더하거나 뺀다.
        if count:
            average = total / count
            for i in range(1, n+1):
                for j in range(m):
                    if array[i][j]:
                        if array[i][j] > average:
                            array[i][j] -= 1
                        elif array[i][j] < average:
                            array[i][j] += 1
    
import sys
n, m, t = map(int, sys.stdin.readline().split())
array = [[]]
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split()))) # array[원판 번호][원판 내 숫자 인덱스]

for rot in range(t):
    Rotate(array)
    Find_adjacent_number(array)

result = 0
for i in range(1, n+1):
    for j in range(m):
        result += array[i][j]

print(result)