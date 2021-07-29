blocks = [x for x in range(1, 50001, 1000)]
d = [[] for _ in range(500001)]
total = 0
count = 0
for block in blocks:
    total += block
    for i in range(1, total):
        if 0 < (len(d) - i + block) < 500000 and d[len(d) - i]:
            d[len(d) - i + block].append(d[len(d) - i] + [block])
        count += 1
    d[block].append(block)

print(d[50000])
print(count)