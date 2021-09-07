# https://www.acmicpc.net/problem/16120
# 접근 방법
# 주어진 문자열을 하나씩 stack에 저장하면서 매번 stack에 저장된 가장 마지막 4개의 문자열이 ppap일 경우 이를 모두 pop하고 p를 삽입한다.
# 모든 문자열을 탐색한 뒤, stack에 p만 남아있다면 PPAP를, 아닌 경우 NP를 출력한다.
import sys
input = sys.stdin.readline
string = [x for x in input().rstrip()]
stack = []
for x in string:
    stack.append(x)
    while len(stack) >= 4 and ''.join(stack[-4:]) == 'PPAP':
        for _ in range(4):
            stack.pop()
        stack.append('P')

if stack == ['P']:
    print('PPAP')
else:
    print('NP')