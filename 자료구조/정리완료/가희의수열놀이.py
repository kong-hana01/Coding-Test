# acmicpc.net/problem/17162
# 접근 방법
# 1이 나올 경우 주어진 값을 하나씩 stack에 저장한 뒤, 리스트를 하나 만들어 mod로 나눌 때의 나머지에 해당하는 인덱스의 값에 몇 번째에 추가됐는 지를 추가한다.
# 2가 나올 경우 스택에서 값을 빼내어 해당 인덱스에 해당하는 값을 하나 뺀다.
# 3이 나올 경우 나머지 리스트의 값을 모두 확인한 뒤, 비어있는 리스트가 있다면 0, 없다면 현재 stack의 길이와 각 인덱스에 해당하는 리스트의 마지막 값 중 가장 작은 값을 빼내어 이를 출력한다.
import sys
input = sys.stdin.readline
q, mod = map(int, input().split())
arr = []
dp = [[] for _ in range(mod)]
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        dp[query[1]%mod].append(len(arr))
        arr.append(query[1]%mod)
    elif query[0] == 2:
        if arr:
            x = arr.pop()
            dp[x].pop()
    else:
        min_count = len(arr)
        check = True
        for x in dp:
            if not x:
                print(-1)
                check = False
                break
            min_count = min(x[-1], min_count)
        if check:
            print(len(arr) - min_count)