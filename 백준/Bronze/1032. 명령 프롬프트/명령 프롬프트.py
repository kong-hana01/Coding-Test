n = int(input())
arr = [input() for _ in range(n)]
result = ""
for i in range(len(arr[0])):
    s = arr[0][i]
    for j in range(1, n):
        if s != arr[j][i]:
            s = "?"
            break
    result += s
print(result)