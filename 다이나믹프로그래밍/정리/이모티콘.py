# https://www.acmicpc.net/problem/14226
# 접근 방법
# s x 2의 길이를 가지는 dp를 s+1로 초기화하고 dp[1]에는 1의 값을 저장한다. dp의 값은 스크린에 있는 이모티콘의 개수를 의미하고 처음은 화면에 있는 이모티콘을 복사하는 것을 가정한다.
# 세가지 연산을 진행할 때마다 큐에 [클립보드에 있는 이모티콘의 개수, 화면에 있는 이모티콘의 개수, 연산 시간]을 저장하여 이를 가지고 연산을 반복한다.
# 단, 큐에 값을 삽입할 때는 dp의 값보다 작은 경우만 삽입한다.
# 이때 화면에 있는 이모티콘의 개수가 s와 같다면 이를 종료하고 연산 시간을 출력한다.
from collections import deque

s = int(input())
dp = [s+1 for _ in range(s*2)]
dp[1] = 1
queue = deque([])
queue.append([1, 1, 1])
while queue:
    clipboard, screen, time = queue.popleft()
    
    if clipboard < screen < s:
        queue.append([screen, screen, time+1])

    if clipboard + screen < s*2:
        dp[clipboard+screen] = min(time+1, dp[clipboard+screen])
        queue.append([clipboard, clipboard+screen, time+1])
    
    if screen - 1 > 0:
        if dp[screen-1] >= time+1:
            dp[screen-1] = time+1
            queue.append([clipboard, screen-1, time+1])
    
    # print(dp, queue)
    if dp[s] != s+1:
        print(dp[s])
        break