arr = [int(x) for x in input()]
arr.sort(reverse=True)
for x in arr:
    print(x, end='')