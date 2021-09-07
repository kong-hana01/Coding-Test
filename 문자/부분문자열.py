# https://www.acmicpc.net/problem/16916
# 접근방법 -> 시간 초과
# in 연산자를 통해 p가 s의 부분 문자열인지 확인한다.
import sys
input = sys.stdin.readline
# s = input().rstrip()
# p = input().rstrip()
# s = 'abas'*100000
# p = 'aba9'*100000
# if p in s:
#     print(1)
# else:   
#     print(0)
s = [x for x in input().rstrip()]
p = [x for x in input().rstrip()]
