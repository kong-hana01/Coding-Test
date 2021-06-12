from collections import deque

# 중복된 값들을 체크하며 단계를 하나하나 점검한다면 최대 100,000번의 연산으로 문제를 해결할 수 있다.

# 최적화를 위해 불필요한 연산을 제거한다. -> 오히려 문제 발생 -> 안함
# 수빈이의 위치 x 2가 수빈이 동생의 위치보다 적은 숫자인 경우 : 무조건 곱해준다.
# 수빈이가 동생보다 높은 숫자에 있는 경우 : 무조건 빼준다.
# 수빈이가 0또는 1인 경우 : 더해준다. (1인 경우는 곱하거나 더해도 상관 없다.)

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