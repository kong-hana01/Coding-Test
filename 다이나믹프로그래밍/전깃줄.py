# https://www.acmicpc.net/problem/2565
# 접근 방법
# 증가하는 부분수열의 최대 길이를 구한 뒤, 전체 전깃줄의 개수에서 최대길이를 빼주어 없애야하는 전깃줄의 최소 개수를 출력한다.
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
dp = []
for x in arr:
    for i in range(len(dp)):
        if dp[i] > x[1]:
            dp[i] = x[1]
            break
    if not dp or dp[-1] < x[1]:
        dp.append(x[1])
print(n - len(dp))