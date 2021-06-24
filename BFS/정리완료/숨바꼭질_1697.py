from collections import deque

# 중복된 값들을 체크하며 단계를 하나하나 점검한다면 최대 100,000번의 연산으로 문제를 해결할 수 있다.

n, k = map(int,input().split())
visited = [0 for _ in range(100001)]
queue = deque([n])

while True:
    x = queue.popleft()
    if x==k:
        break
        
    elif x+1 <= 100000 and visited[x+1] == 0:
        visited[x+1] = visited[x] + 1
        queue.append(x+1)
        if x+1 == k:
            break

    if 0 <= x-1 and  visited[x-1] == 0:
        visited[x-1] = visited[x] + 1
        queue.append(x-1)
        if x-1 == k:
            break
        
    if x*2 <= 100000 and visited[x*2] == 0:
        visited[x*2] = visited[x] + 1
        queue.append(x*2)
        if x*2 == k:
            break

print(visited[k])