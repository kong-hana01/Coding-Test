# https://www.acmicpc.net/problem/16936
# 접근 방법
# 모든 경우의 수에 대해 처리한다.
def backtracking(now, result):
    if not seq:
        return result
    
    if now % 3 == 0 and now // 3 in seq:
        next = now // 3
        seq.remove(next)
        is_finish = backtracking(next, result + [next])
        if is_finish:
            return is_finish
        seq.add(next)

    if now * 2 in seq:
        next = now * 2
        seq.remove(next)
        is_finish = backtracking(next, result + [next])
        if is_finish:
            return is_finish
        seq.add(next)
    return

n = int(input())
arr = list(map(int, input().split()))
seq = set(arr)
for x in arr:
    seq.remove(x)
    result = backtracking(x, [x])
    if result:
        print(*result)
        break
    seq.add(x)