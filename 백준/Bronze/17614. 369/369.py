# https://www.acmicpc.net/problem/17614
n = int(input())
result = 0
for i in range(1, n+1):
    value = str(i)
    result += value.count("3") + value.count("6") + value.count("9")
print(result)