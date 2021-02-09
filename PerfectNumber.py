a = int(input())
i = 1
s = 0
while i < a:
    if a % i == 0:
        s += i
    i += 1
if a == s:
    print("Число ", a, " - совершенное!")
else:
    print("Число ", a, " - несовершенное!")