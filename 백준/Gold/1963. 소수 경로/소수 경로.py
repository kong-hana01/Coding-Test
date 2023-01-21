# https://www.acmicpc.net/problem/1963
# 접근 방법
# 소수를 구한 뒤, bfs를 돌린다.
def find_prime_number():
    prime_number = set([])
    visited = [False for _ in range(10000)]
    now = 1
    while now < 9999:
        now += 1
        if visited[now]:
            continue
        if now >= 1000:
            prime_number.add(str(now))
        visited[now] = True
        next = now * 2
        while next <= 9999:
            visited[next] = True
            next += now
    return prime_number

def bfs(start):
    queue = deque([])
    queue.append([x for x in start])
    visited[int(start)] = 0
    while queue:
        num = queue.popleft()
        now = "".join(num)
        for i in range(4):
            for j in range(10):
                temp = num[:]
                temp[i] = str(j)
                next = "".join(temp)
                if next not in prime_number or visited[int(next)] != -1:
                    continue
                visited[int(next)] = visited[int(now)] + 1
                queue.append(temp)
    


from collections import deque
prime_number = find_prime_number()
tc = int(input())
for _ in range(tc):
    visited = [-1 for _ in range(10000)]
    a, b = input().split()
    bfs(a)
    print(visited[int(b)])
