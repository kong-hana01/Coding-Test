# https://www.acmicpc.net/problem/14002
# 접근 방법
# 다이나믹 프로그래밍을 통해 O(N**2)의 시간복잡도를 가진 부분 수열을 구한다.
n = int(input())
array = list(map(int, input().split()))
dp = [[str(x)] for x in array]
for i in range(n):
    for j in range(i+1, n):
        if array[i] < array[j] and len(dp[i])+1 > len(dp[j]):
            dp[j] = dp[i] + [str(array[j])]

dp.sort(key=lambda x: len(x))
print(len(dp[-1]))
print(' '.join(dp[-1]))