n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dist = [0]
for i in range(n-1):
    dist.append(arr[i+1] - arr[i])
dist.sort()
for i in range(k-1):
    dist.pop()
print(sum(dist) + k)