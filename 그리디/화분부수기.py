# https://www.acmicpc.net/problem/3088
# 접근방법
# 가장 왼쪽부터 순서대로 화분을 깨며 해당하는 숫자를 인덱스를 통해 dp에 1을 저장한다.
# 만약 화분을 깼을 때 이미 깬 화분의 숫자를 포함하고 있다면 그 화분은 숫자를 더하지 않는다.
# 만약 화분을 깼을 때 숫자가 없다면 dp에 해당 값들을 모두 저장하고 카운트를 추가한다.
# 모든 화분을 탐색한 뒤, 카운트를 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
pot = [list(map(int, input().split())) for _ in range(n)]
count = 0
dp = [0 for _ in range(10**6 + 1)]
for a, b, c in pot:
    if not dp[a] and not dp[b] and not dp[c]:
        count += 1
    dp[a], dp[b], dp[c] = 1, 1, 1
print(count)