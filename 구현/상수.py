# https://www.acmicpc.net/problem/2908
# 접근 방법
# 세자리 수 중 거꾸로 한 수가 작은 수를 출력한다.
a, b= input().split()
a = a[::-1]
b = b[::-1]
print(int(a) if int(a) > int(b) else int(b))