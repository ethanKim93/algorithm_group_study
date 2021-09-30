st = "0000000111100000011000000111100110000110000111100111100111111001100111"

for i in range(0, len(st), 7):
    num = st[i:i+7]
    total = 0
    for j in range(7):
        if num[j] == "1":
            total += 2 ** (6 - j)
    print(total)
