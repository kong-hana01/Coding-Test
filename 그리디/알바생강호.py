# https://www.acmicpc.net/problem/1758
# 접근 방법
# 스타박스에 서있는 사람들을 원래 주려했던 돈을 기준으로 내림차순 정렬한 뒤, 등수를 하나씩 더해가며 받을 수 있는 팁의 최댓값을 출력한다.
import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse = True)
result = 0
for rank, x in enumerate(arr):
    if x - rank <= 0:
        break
    result += x - rank
print(result)