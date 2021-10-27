# https://www.acmicpc.net/problem/16228
# 접근방법 -> 시간관계상 다음에 진행
# 스택자료구조를 활용해 값을 하나씩 입력하다 (가 있는 상태에서(count로 확인) )가 등장하면 (가 등장할 때까지 stack을 pop하고 이를 연산하고 다시 stack에 저장한다.
# (의 개수가 없고, 숫자가 저장되어있으며 길이가 2 이상인 경우 stack의 마지막 이전 값이 무엇인지 확인해 해당 연산을 동작한다.
def oper(array):
    arr = []
    while array:
        x = array.pop()


s = input()
stack = []
count = 0
for x in s:
    stack.append(x)
    if stack and stack[-1] == '(':
        count += 1
    if stack and stack[-1] == ')':
        temp = []
        check = True
        while stack and check:
            x_ = stack.pop()
            temp.append(x)
            if x == '(':
                check = False
        while temp:

        count -= 1