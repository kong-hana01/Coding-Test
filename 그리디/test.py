# 1. n > k인 경우 플러그를 뺄 필요가 없으므로 0 출력
# 2-1. n < k인 경우 n만큼 플로그를 꽂고 뒤에 현재 플러그에 꽂은 전기 용품이 있다면 그대로 놔두고 다음 전기 용품을 확인한다.
# 2-2. n < k인 경우 n만큼 플로그를 꽂고 뒤에 현재 플러그에 꽂은 전기 용품이 없다면 계속해서 다음 전기용품을 확인하면서 현재 플러그에 꽂은 전기 용품 중 가장 먼저 나오는 전기 용품을 제외한 나머지 전기 용품들을 탐색한다.
# 2-3. 이후 가장 늦게 나오거나 나오지 않은 전기 용품 중에서 하나를 뽑아 다음 전기 용품을 꽂는다.
# 해당 문제는 n과 k의 범위가 최대 100이기에 삼중 반복문을 사용하더라도 괜찮다.

import sys
n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
multitap = []
priority = [0 for _ in range(n)] # 멀티탭에 꽂혀있는 전기용품에 대해 우선순위를 정해준다.
unplug_count = 0

if n >= k:
    print(0)
else:
    # 써야할 전기용품을 차례대로 탐색한다.
    for i in range(len(array)):
        # 해당 전기 용품이 현재 멀티탭에 꽂혀있는지 확인한다.
        if array[i] not in multitap:
            # 현재 멀티탭에 꽂혀있는 전기 용품이 구멍 개수보다 작은 지 확인한다.
            if len(multitap) < n:
                multitap.append(array[i]) # 현재 멀티탭에 꽂혀있는 전기 용품이 구멍 개수보다 작은 경우 멀티탭에 꽂는다.
            # 이미 남아있는 멀티탭 구멍이 없는 경우
            else:
                # 현재까지 탐색한 전기용품 다음 인덱스의 전기용품들을 확인한다.
                count_of_electonic_in_multitap = 0
                for j in range(i, len(array)):
                    # 만약 탐색 중간에 멀티탭에 꽂혀있는 전기 용품을 발견한다면 해당 전기 용품의 우선순위를 정해준다.                 
                    for k in range(len(multitap)):
                        if array[j] == multitap[k] and priority[k] == 0:
                            priority[k] = j
                            count_of_electonic_in_multitap += 1
                # 만약 멀티탭에 꽂혀있는 전기용품을 발견하지 못한 게 있다면 멀티탭에 꽂혀있는 전기 용품 나중에 사용하지 않는 전기용품을 빼준다.
                if count_of_electonic_in_multitap == n:
                    multitap.pop(priority.index(max(priority)))
                # 멀티탭에 꽂혀있는 전기
                else:
                    multitap.pop(priority.index(0))
                priority = [0 for _ in range(n)]
                unplug_count += 1 # 플러그를 하나 뽑아준다.
                multitap.append(array[i])  # 이후 멀티탭에 전기용품을 꽂아준다.
    print(unplug_count)


