a = int(input())
b = int(input())
i = a
s = 0
while i <= b:
    for x in range(len(str(i))):
        s += int(str(i)[x])**len(str(i))
    if i == s:
        print(i)
    i += 1
    s = 0