# https://www.acmicpc.net/problem/1422
# 접근 방법
# 다음의 우선순위를 고려하여 정렬한다.
# 1. 자리수를 고려하여 정렬한다. -> 자리수가 가장 많은 것을 반복적으로 사용해 큰 수를 만든다.
# 2. 자리수가 동일한 경우에는 숫자를 기준으로 정렬한다. -> 자리수가 가장 많고, 가장 큰 수를 반복적으로 사용해 큰 수를 만든다.
# 정렬된 숫자들을 확인한 뒤 최소한의 자리수로 높은 숫자가 있는 것을 기준으로 하나씩 뽑아서 숫자를 만들어간다.
# 이때 우선순위가 가장 높은 숫자가 등장한다면 n-k+1번만큼 뒤에 붙인다.
# 모든 숫자를 다 붙인 뒤 값을 출력한다.
k, n = map(int, input().split())
arr = [[] for _ in range(11)]
for _ in range(k):
    num = input()
    arr[len(num)].append(num)

priorityNumber = 0
for i in range(len(arr)):
    arr[i].sort()
    priorityNumber = max(priorityNumber, int(arr[i][-1]) if arr[i] else 0)

result = ''
check_prior = False
for i in range(k):
    now = ''
    for j in range(len(arr)):
        if not now or (arr[j] and int(now + arr[j][-1]) < int(arr[j][-1] + now)): # now가 없거나 두 값을 비교해 우선순위를 비교하여 더 큰 값을 갱신한다.
            now = arr[j][-1] if arr[j] else now
    arr[len(now)].pop()
    if int(now) == priorityNumber and not check_prior:
        for _ in range(n-k+1):
            result = result + now
        check_prior = True
        
    else:
        result = result + now
print(result)