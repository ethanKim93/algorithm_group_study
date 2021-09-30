for case in range(int(input())):
    N = float(input())
    bits = []
    flag = True
    for i in range(1, 13):
        num = 1 / (2**i)
        if N >= num:
            N -= num
            bits.append("1")
        else:
            bits.append("0")

        if N == 0:
            break

    else:
        flag = False

    if flag:
        print("#{} {}".format(case + 1, ''.join(bits)))
    else:
        print("#{} overflow".format(case + 1))
