var = [8, 89, 36, 24, 48, 54, 5, 70, 63, 11]
for x in range(len(var) - 2):
    for i in range(len(var) - 1):
        if var[i] > var[i + 1]:
            var[i + 1] = var[i + 1] + var[i]
            var[i] = var[i + 1] - var[i]
            var[i + 1] = var[i + 1] - var[i]
x = int(input())
i = 0
a = len(var) - 1
b = int(a / 2)
while var[b] != x and i < a:
    if x > var[b]:
        i = b + 1
    else:
        a = b - 1
    b = int((a + b) / 2)
if i > a:
    print("Числа ", x, " нет в списке!")
else:
    print(b)