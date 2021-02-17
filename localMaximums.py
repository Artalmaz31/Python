a = b = i = m = 0
while True:
    a = int(input())
    if a == 0: break
    if a > b:
        b = a
        if i > m:
            m = i
        i = 0
    elif a < b:
        i += 1 
        b = a
print(m)