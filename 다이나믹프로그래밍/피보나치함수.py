# https://www.acmicpc.net/problem/1003
# 접근 방법
# n의 최대값만큼 dp 테이블을 초기화한 뒤, 0과 1인덱스의 dp 테이블에 [1, 0], [0, 1]을 각각 입력한다.
# 이후 n이 2부터 1씩 증가할 때마다 0과 1을 호출한 횟수를 dp 테이블에 저장하고 각 테스트 케이스마다 이를 출력한다.

dp = [[0, 0] for _ in range(41)] 

for i in range(2):
    dp[i][i%2] += 1

def fibonacci(x):
    if dp[x] != [0, 0]:
        return dp[x]
    elif x == 0:
        return [1, 0]
    elif x == 1:
        return [0, 1]
    else:
        for i in range(1, 3):
            data = fibonacci(x-i)
            dp[x][0] += data[0]
            dp[x][1] += data[1]
        return dp[x]

for t in range(int(input())):
    n = int(input())
    fibonacci(n)
    print(dp[n][0], dp[n][1])