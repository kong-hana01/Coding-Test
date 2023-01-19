# https://www.acmicpc.net/problem/2015
# 접근 방법
# 부분합의 개수를 딕셔너리에 넣어가며 구한 뒤, 
# 부분합을 다시 구해가며 k + 해당 값까지의 부분합의 개수가 총 몇개인지 누적하며 구한다.
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
count_of_prefix_sum = {k:0}
prefix_sum = 0
for x in arr:
    prefix_sum += x
    if prefix_sum not in count_of_prefix_sum:
        count_of_prefix_sum[prefix_sum] = 0
    count_of_prefix_sum[prefix_sum] += 1

result = count_of_prefix_sum[k]
prefix_sum = 0
for x in arr:
    prefix_sum += x
    count_of_prefix_sum[prefix_sum] -= 1
    if prefix_sum + k in count_of_prefix_sum:
        result += count_of_prefix_sum[prefix_sum + k]
    
print(result)