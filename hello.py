add = 0
a = 0
while a <= 1000:
    a = a + 1
    while a % 3 == 0:
        add = add + a
    else: continue

print(add)