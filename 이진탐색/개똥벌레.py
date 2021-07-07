# https://www.acmicpc.net/problem/3020
# 접근 방법
# 주어진 장애물의 크기를 받을 때 짝수번째로 입력 받는 값은 h에서 뺀 값을 받는다.
# 1부터 주어진 h를 하나씩 탐색하며 주어진 장애물의 홀수번째는 그 값에 해당되면 장애물을 파괴한 개수에 +1, 짝수번째는 그 값에 해당이 안되면 장애물을 파괴한 개수에 +1을 해준다.
# 장애물을 파괴한 개수가 같은 게 있다면 그 구간의 수를 +1 해주고, 장애물을 파괴한 개수가 더 작은 게 있다면 이를 초기화하고 그 구간의 개수를 1로 한다.
import sys

n, height = map(int, sys.stdin.readline().split())
array = [0]

for i in range(1, n+1):
    x = int(sys.stdin.readline())
    if i % 2 == 0: # 짝수번째로 입력받는 값
        array.append(height-x)
    else: # 홀수번째로 입력받는 값
        array.append(x)

obstacle = n # 장애물 개수 초기화
countOfinterval = 0 # 구간의 개수 초기화
for h in range(1, height+1):
    
