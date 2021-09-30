for case in range(int(input())):
    N, st = input().split()

    bits_list = []
    for i in st:
        asc = ord(i)
        integer = asc - 48 if asc <= 57 else asc - 55
        for j in range(4):
            bits_list.append(str(integer >> (3 - j) & 1))

    bits = ''.join(bits_list)

    print("#{} {}".format(case+1, bits))