a, b = map(int, input().split())
even, odd = 0, 0
for i in range(a, b+1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, odd)
