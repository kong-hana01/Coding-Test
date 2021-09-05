# https://www.acmicpc.net/problem/2343
# 접근방법
# 블루레이의 길이가 최대 10억까지 가능하기 때문에 시작점을 0, 끝점을 레슨의 모든 시간 합계로 하는 이진탐색을 진행한다.
# 레슨을 하나씩 탐색하며 블루레이에 얼만큼 담을 수 있는지 확인한 뒤, 사용한 블루레이의 개수가 M을 초과할 경우 start를 mid+1로 초기화한 뒤, 중간점을 다시 저장한다.
# 사용한 블루레이의 개수가 M이하일 경우에 결과값과 이를 비교해 작은 값을 저장하고 end값을 mid-1로 초기화한 뒤, 중간점을 다시 저장한다.
# start가 end보다 커지는 시점에 이를 종료하고 결과값을 출력한다.

n, m = map(int, input().split())
lesson = list(map(int, input().split()))

start = max(lesson)
end = sum(lesson)
result = sum(lesson)

while start <= end:
    mid = (start+end) // 2 
    count = 1
    bluelay = mid
    
    for x in lesson:
        if bluelay < x:
            count += 1
            bluelay = mid
        bluelay -= x
    
    if count > m:
        start = mid+1
    
    else:
        end = mid-1
        result = min(mid, result)

print(result)