# https://www.acmicpc.net/problem/2011
# 접근 방법
# 최소 2글자가 있다면 다이나믹 프로그래밍을 사용해서 이를 처리한다.
code = input()
dp = [0 for _ in range(len(code))]
dp[0] = 1
is_correct = True
if int(code[0]) == 0:
    is_correct = False

if len(code) >= 2:
    if int(code[:2]) in [0, 30, 40, 50, 60, 70, 80, 90] or int(code[-2:]) in [0, 30, 40, 50, 60, 70, 80, 90]:
        is_correct = False
    else:
        if 11 <= int(code[:2]) <= 26 and code[1] != '0': #  and (len(code) >= 3 and code[2] != '0'):
            dp[1] = 2
        else:
            dp[1] = 1
        for i in range(2, len(code)):
            if code[i] != '0':
                dp[i] = dp[i-1] % 1000000
            if 10 <= int(code[i-1:i+1]) <= 26:
                dp[i] = (dp[i] + dp[i-2]) % 1000000

    # dp[-1] = dp[-2]
    # dp[-1] += dp[-3] if 11 <= int(code[-2:]) <= 26 else 0

print(dp[-1] % 1000000 if is_correct else 0)