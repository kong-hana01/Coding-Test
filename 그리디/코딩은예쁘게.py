# https://www.acmicpc.net/problem/2879
# 접근방법
# 현재 줄에 있는 탭과 올바른 탭을 비교하며 현재 상태에 따라 편집횟수를 저장한다.
# 1. 증가상태나 삭제상태에서 현재 줄에 있는 탭의 개수와 올바른 탭의 개수가 같다면 패스 상태(0)로 변환 후 패스한다.
# 2. 여태 바꾸지 않았거나 증가상태라면 현재 줄에 있는 탭의 개수가 올바른 탭의 개수보다 크다면 개수를 하나 줄이고, 편집횟수를 하나 늘린다음 삭제 상태(1)로 변경한다.
# 2-1. 삭제 상태에서 현재 줄에 있는 탭의 개수가 올바른 탭의 개수보다 크다면 개수를 하나 줄이고 패스한다.
# 3.여태 바꾸지 않았거나 삭제상태라면 현재 줄에 있는 탭의 개수가 올바른 탭의 개수보다 작다면 개수를 하나 늘리고, 편집횟수를 하나 늘린다음 증가 상태(2)로 변경한다.
# 3-1. 증가 상태에서 현재 줄에 있는 탭의 개수가 올바른 탭의 개수보다 작다면 개수를 하나 늘리고 패스한다.
# 모든 탐색이 끝나면 편집 횟수를 출력하고 종료한다.


n = int(input())
now_tab = list(map(int, input().split()))
correct_tab = list(map(int, input().split()))

count = 0
condition = [0, 1, 2]
check = 0
while now_tab != correct_tab:
    for i in range(n):
        if now_tab[i] == correct_tab[i]:
            check = 0
        elif now_tab[i] > correct_tab[i]:
            if check != 1:
                count += 1
                now_tab[i] -= 1
                check = 1
            else:
                now_tab[i] -= 1
        else:
            if check != 2:
                count += 1
                now_tab[i] += 1
                check = 2
            else:
                now_tab[i] += 1
    check = 0

print(count)