# https://www.acmicpc.net/problem/10942
# 접근방법
# 홀수 개의 부분 수열이 팰린드롬인지 확인하기 위해선 가운데에 있는 수를 기준으로 양 옆의 숫자가 같은지 차례로 확인하면 된다.
# ex) 홀수: 1 2 1 3 1 2 1 -> 3을 기준으로 1, 1이 같은지 확인하고 같으면 1, 다르면 0을 저장해준다음 2, 2가 같은지 확인하고, 1, 1이 같은지 확인하며 차례로 저장해나간다.
# 짝수 개의 부분 수열이 팰린드롬인지 확인하기 위해선 가운데를 기준으로 양옆에 있는 숫자가 같은지 차례로 확인하면 된다.
# ex) 짝수: 1 2 2 1 -> 2, 2가 같은 지 확인하고 값을 저장한 뒤, 1, 1이 같은 지 확인하고 값을 저장하는 식으로 한다.
def check_palindrome(s, e):
    if dp[s][e] == 1:
        return 1
    elif not dp[s][e]:
        return 0
    if s+1 <= e-1:
        if not check_palindrome(s+1, e-1):
            dp[s][e] = 0
            return 0
        if array[s] == array[e]:
            dp[s][e] = 1
            return 1
        else:
            dp[s][e] = 0
            return 0
    else:
        if array[s] == array[e]:
            dp[s][e] = 1
            return 1
        else:
            dp[s][e] = 0
            return 0

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
dp = [[1 if i == j else -1 for j in range(n)] for i in range(n)]
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(check_palindrome(s-1, e-1))
