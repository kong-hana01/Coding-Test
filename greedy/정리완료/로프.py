
# n = int(input())
# rope = sorted([int(input()) for _ in range(n)], reverse=True)
n = int(input())
rope = sorted([i for i in range(n)], reverse=True)


# n = 7
# rope = sorted([10, 15, 15, 9, 9, 9, 1000], reverse = True)
k = rope[0]

# for i in range(1, len(rope)):
#     if min(k) * len(k) < rope[i] * (len(k)+1):
#         k.append(rope[i])
#     else:
#         break

w = 0
for i in range(n-1, -1, -1):
    if rope[i] * (i + 1) > w:
        w = rope[i] * (i + 1)

print(w)
#print(rope)