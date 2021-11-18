# https://www.acmicpc.net/problem/6068
# 접근 방법
# 주어진 일을 끝내야하는 시간을 기준으로 내림차순 정렬한다.
# 이후 일을 하나씩 탐색해나가며 여유 시간을 갱신해나간다.
# 여유 시간은 다음과 같이 갱신한다.
# min(현재까지의 여유시간, 끝내야하는 마감시간) - 현재 탐색 중인 일을 하는데 필요한 시간

n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
work.sort(key=lambda x:x[1], reverse = True)
spare_time = work[0][1]
for x in work:
    spare_time = min(x[1], spare_time) - x[0]
if spare_time >= 0:
    print(spare_time)
else:
    print(-1)