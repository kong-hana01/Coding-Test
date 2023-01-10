# https://www.acmicpc.net/problem/1259
# 접근방법
# 재귀적으로 문제를 풀어본다.
def check_pel(s, start, end):
    if start >= end:
        return "yes"
    if s[start] != s[end]:
        return "no"
    return check_pel(s, start+1, end-1)

while True:
    s = input()
    if s == '0':
        break
    print(check_pel(s, 0, len(s)-1))