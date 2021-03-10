a = int(input())
b = int(input())
while a > 0 and b > 0 and a + b >= 3:
    c = 0
    l = [''] * 3
    while c < 3:
        if a > b:
            if c == 2 and 'b' not in l:
                b -= 1
                l[2] = 'b'
            else:
                a -= 1
                l[c] = 'a'
        else:
            if c == 2 and 'a' not in l:
                a -= 1
                l[2] = 'a'
            else:
                b -= 1
                l[c] = 'b'
        c += 1
    print(*l)
    print('-----------')
print(a, b)