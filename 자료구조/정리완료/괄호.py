# https://www.acmicpc.net/problem/9012
import sys
t = int(sys.stdin.readline())

for _ in range(t):
    parenthesis_string = sys.stdin.readline().rstrip()
    array = [parenthesis_string[0]]
    if array[0] == ')':
        print('NO')
        continue
    for x in parenthesis_string[1:]:
        if array and array[-1] == '(' and x == ')':
            array.pop()
        else:
            array.append(x)
    if array:
        print('NO')
    else:
        print('YES')