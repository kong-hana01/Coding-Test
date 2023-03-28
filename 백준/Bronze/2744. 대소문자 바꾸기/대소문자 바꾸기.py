alpha = {}
for i in range(ord("A"), ord("Z")+1):
    alpha[chr(i)] = chr(i + ord("a") - ord("A"))
    alpha[chr(i + ord("a") - ord("A"))] = chr(i)
for x in input():
    print(alpha[x], end = "")
