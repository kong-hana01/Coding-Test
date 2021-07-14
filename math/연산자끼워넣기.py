# https://www.acmicpc.net/problem/14888
# 접근 방법
# 순열 라이브러리를 활용해 모든 경우에 수에 대해 주어진 숫자에 적용해보고 최대값과 최소값을 출력한다.
from itertools import permutations
n = int(input())
array = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

operator = []
for _ in range(plus):
    operator.append('+')
for _ in range(minus):
    operator.append('-')
for _ in range(multiply):
    operator.append('*')
for _ in range(divide):
    operator.append('/')


max_value = -1000000001
min_value = 1000000001
for oper in list(permutations(operator)):
    value = array[0]
    # print('oper:', oper)
    for i in range(1, n):
        if oper[i-1] == '+':
            value += array[i]
        elif oper[i-1] == '-':
            value -= array[i]
        elif oper[i-1] == '*':
            value *= array[i]
        else:
            if value < 0:
                value = -(abs(value) // array[i])
            else:
                value = value // array[i]
    # print(value)
    max_value = max(max_value, value)
    min_value = min(min_value, value)

print(max_value)
print(min_value)
