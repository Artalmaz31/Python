var1 = [5, 2, 7, 4, 6, 9, 8, 1, 3]
for x in range(len(var1) - 2):
    for i in range(len(var1) - 1):
        if var1[i] > var1[i + 1]:
            var1[i + 1] = var1[i + 1] + var1[i]
            var1[i] = var1[i + 1] - var1[i]
            var1[i + 1] = var1[i + 1] - var1[i]
print(*var1)