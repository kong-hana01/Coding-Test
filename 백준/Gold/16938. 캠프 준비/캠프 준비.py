# https://www.acmicpc.net/problem/16938
# 접근 방법
# 백트래킹을 사용해 문제를 해결한다.
def backtracking(problem_set, now_index):
    containing_idx_to_str = "".join(containing_idx)
    if len(problem_set) >= 2 and l <= sum(problem_set) <= r and max(problem_set) - min(problem_set) >= x and containing_idx_to_str not in visited:
        global result
        result += 1
        visited.add(containing_idx_to_str)

    for i in range(now_index+1, n):
        containing_idx[i] = "1"
        backtracking(problem_set + [rank[i]], i)
        containing_idx[i] = "0"
        backtracking(problem_set, i)

n, l, r, x = map(int, input().split())
rank = list(map(int, input().split()))
result = 0
visited = set([])
containing_idx = ["0" for _ in range(n)]
backtracking([], -1)
print(result)