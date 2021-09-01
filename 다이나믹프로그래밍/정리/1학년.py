# 접근방법
# 1. dp 테이블을 0부터 20까지 초기화하고 처음 주어진 수의 인덱스에 1을 저장한다.
# 2. 주어진 수를 하나씩 탐색하며 더하고 뺀 값의 인덱스에 +1씩 더해준다.
# 2-1. 이때 0과 20 사이의 범위를 벗어나면 값을 저장하지 않는다.
# 3. 주어진 수를 모두 탐색하고 dp 테이블 내의 모든 값을 합한 뒤, 출력한다.
import sys
n = int(input())
array = list(map(int, sys.stdin.readline().split()))
dp = [0] * 21
dp[array[0]] = 1

# for x in array[1:n-1]:
#     temp = []
#     for i in range(len(dp)):
#         if dp[i] != 0:
#             if i+x <= 20:
#                 for _ in range(dp[i]):
#                     temp.append(i+x)
#             if i-x >= 0:
#                 for _ in range(dp[i]):
#                     temp.append(i-x)
#     dp = [0] * 21
#     for t in temp:
#         dp[t] += 1

# print(dp[array[n-1]])



for x in array[1:n-1]:
    temp_p = [dp[i-x] if i-x >= 0 else 0 for i in range(len(dp))]
    temp_m = [dp[i+x] if i+x <= 20 else 0 for i in range(len(dp))]
    for i in range(len(dp)):
        dp[i] = temp_p[i] + temp_m[i]

print(dp[array[n-1]])