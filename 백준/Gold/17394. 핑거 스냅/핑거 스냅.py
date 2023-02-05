# https://www.acmicpc.net/problem/17394
# 접근 방법
# 소수로 만든 뒤 문제를 해결한다.
def find_prime_number():
    visited = [False for _ in range(100001)]
    prime_numbers = []
    prime_number = 2
    while prime_number <= 100000:
        if visited[prime_number]:
            prime_number += 1
            continue
        visited[prime_number] = True
        prime_numbers.append(prime_number)
        not_prime_number = prime_number * 2
        while not_prime_number <= 100000:
            visited[not_prime_number] = True
            not_prime_number += prime_number
        prime_number += 1
    return prime_numbers

from collections import deque
prime_numbers = find_prime_number()
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    visited = [-1 for _ in range(3000001)]
    queue = deque([])
    queue.append(n)
    visited[n] = 0
    find_value = []
    for x in prime_numbers:
        if a<=x<=b:
            find_value.append(x)
    if not find_value:
        print(-1)
        continue
    while queue:
        now = queue.popleft()
        for next in [now // 2, now // 3, now + 1, now - 1]:
            if 0<=next<=3000000 and visited[next] == -1:
                visited[next] = visited[now] + 1
                queue.append(next)
    result = 100000
    for x in find_value:
        if visited[x] == -1:
            continue
        result = min(result, visited[x])
    if result == 100000:
        print(-1)
    else:
        print(result)