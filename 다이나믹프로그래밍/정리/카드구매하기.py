# https://www.acmicpc.net/problem/11052
# 접근방법
# n개의 카드를 구매할 때 구매하는 경우의 수를 크게 세가지로 분류할 수 있다.
# 1. Pn의 카드팩을 구매하는 방법
# 2. Pk * x의 카드팩을 구매하는 방법
# 3. (P(k-1) + P(n - k + 1))의 카드팩을 구매하는 방법
# 시간복잡도를 고려해보면 첫번째 방법은 n, 두번째 방법은 nlogn, 세번째 방법은 N**2의 연산횟수를 가진다. 따라서 최대 N**2의 연산횟수로 해당 문제를 해결할 수 있다.
# 최대연산 횟수: n + nlogn + n**2

n = int(input())
array = list(map(int, input().split()))

d = [0] * (n+1)
for i in range(1, n+1):
    d[i] = max(array[i-1], d[i]) # 경우의 수 1
    
    for j in range(i, n+1, i): # 경우의 수 2
        d[j] = j//i * d[i]
    
    # 경우의 수 3
    start = 1
    end = i - 1
    while start < end:
        d[i] = max(d[start] + d[end], d[i])
        start += 1
        end -= 1
        
print(d[n])