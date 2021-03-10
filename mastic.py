a, b, c, N = input().split()
a, b, c, N = int(a), int(b), int(c), int(N)
l = sorted([a, b, c])
a, b, c = l[2], l[1], l[0]
m = 0
while m < N:
    if(N - m >= a):
        m += a
        print('+', a)
    elif(N - m >= b):
        m += b
        print('+', b)
    else:
        m += c
        print('+', c)