s = input()
result = 0
alpha = ["a", "e", "i", "o", "u"]
for x in s:
    if x in alpha:
        result += 1
print(result)