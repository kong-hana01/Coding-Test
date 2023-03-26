n, t = map(int, input().split())
arr = list(map(int, input().split()))
print(" ".join(list(map(str, map(lambda x: x - n*t, arr)))))