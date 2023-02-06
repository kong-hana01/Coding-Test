# https://www.acmicpc.net/problem/17828
# 접근 방법
# 채울 수 있는 가장 큰 수부터 먼저 채워서 문자열을 만든 뒤 이를 뒤집는다.
n, x = map(int, input().split())
num_to_alpha = {i-ord('A')+1: chr(i) for i in range(ord('A'), ord('Z')+1)}
result = []
for i in range(n):
    value = (x - (n-i))
    if x == 0 or value < 0:
        break
    if value >= 25:
        result.append("Z")
        x -= 26
    else:
        result.append(num_to_alpha[value + 1])
        x -= value + 1
if x or len(result) != n:
    print("!")
else:
    print("".join(result[::-1]))