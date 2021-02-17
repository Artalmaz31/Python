a = m = i = 0
while True:
    a = int(input())
    if a == 0: break
    if a == m: 
        i += 1
    elif a > m:
        m = a
        i = 1
print(i)