# https://www.acmicpc.net/problem/4949
# 접근 방법
# 0. 주어진 문자열을 하나씩 탐색하며 괄호는 스텍에 저장한다.
# 1. )나 }가 나온다면 이를 스택 내에 가장 마지막에 있는 값과 비교해 매칭이 되는지 확인한다.
# 2. 매칭이 된다면 pass, 매칭이 안된다면 탐색을 중단하고 no를 출력한다.
# 3. 모든 탐색이 끝나고, 스택에 값이 없다면 yes를 출력한다.
while True:
    s = input()
    if s == ".":
        break
    stack = []
    is_wrong = False
    for x in s:
        if x == "(" or x == "[":
            stack.append(x)
        elif x == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_wrong = True
                break
        elif x == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                is_wrong = True
                break
    if is_wrong or stack:
        print('no')
    else:
        print('yes')
    