# https://www.acmicpc.net/problem/16434
# 접근 방법
# 용사의 max_hp를 기준으로 이진탐색을 진행한다. 초기 start는 1, end는 (1000000 ** 2) x n로 설정한다.
# 그 뒤 N개의 방에 대해서 탐색을 진행하며 용사가 던전을 클리어하면 값을 저장해가며 클리어할 수 있는 최소 max_hp를 구한다.

def battle(cur_hp, a, h, atk):
    number_of_turns = h // atk - 1
    if h % atk:
        number_of_turns += 1
        
    cur_hp = max(cur_hp - (a * number_of_turns), 0)
    return cur_hp

def dungeon(hp, atk):
    cur_hp = hp
    for t, a, h in array:
        if t == 1:
            cur_hp = battle(cur_hp, a, h, atk)
            if not cur_hp:
                return False
        else:
            atk += a
            cur_hp = min(cur_hp + h, hp)
    return True


import sys
n, atk = map(int, sys.stdin.readline().split())
array = []
max_a = 0
max_h = 0
for _ in range(n):
    t, a, h = map(int, sys.stdin.readline().split())
    if t == 1:
        max_a = max(a, max_a)
        max_h = max(h, max_h)
    array.append([t, a, h])

start = 1
end = max_a * max_h * n
max_hp = end
while start <= end:
    mid = (start+end) // 2
    
    if dungeon(mid, atk):
        end = mid - 1
        max_hp = min(max_hp, mid)
    else:
        start = mid + 1
print(max_hp)