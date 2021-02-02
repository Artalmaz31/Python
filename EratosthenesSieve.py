def EratosthenesSieve(x):
    a = x * [1]
    i = 1
    while i < x - 1:
        i += 1
        if a[i] == 1:
            j = i**2
            while j < x:
                a[j] = 0
                j += i
        if a[i] == 1:
            print(i) 
EratosthenesSieve(x = int(input()))