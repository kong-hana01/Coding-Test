# https://www.acmicpc.net/problem/10986
# 접근 방법
# 구간합을 구한 뒤, 첫번째 요소부터 모든 요소까지 더했을 때의 m으로 나눠떨어질 때까지의 개수를 체크한 뒤, 하나씩 값을 탐색하며 문제를 풀어본다.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0 for _ in range(m)]
prefix_sum = [arr[0] % m]
cnt[arr[0] % m] += 1
for i in range(1, n):
    prefix_sum.append((prefix_sum[-1] + arr[i]) % m)
    cnt[prefix_sum[-1]] += 1

result = cnt[0]
for i in range(1, n):
    cnt[prefix_sum[i-1]] -= 1
    result += cnt[prefix_sum[i-1]]
print(result)