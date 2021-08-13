def itoa(n):
    ascii = [i for i in range(48, 58)]
    num = ''
    while True:
        if n == 0:
            break
        for j, k in enumerate(ascii):
            if n % 10 == j:
                num += chr(k)
        n //= 10
    print(num[::-1])

a = itoa(1234)
