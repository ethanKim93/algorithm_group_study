st = "0F97A3"

bits_list = []
for i in st:
    asc = ord(i)
    integer = asc - 48 if asc <= 57 else asc - 55
    for j in range(4):
        bits_list.append(str(integer >> (3 - j) & 1))

bits = ''.join(bits_list)

for i in range(0, len(bits), 7):
    seven_bits = bits[i:i+7]
    total = 0
    for j in range(len(seven_bits)):
        if seven_bits[j] == "1":
            total += 2 ** (len(seven_bits) - 1 - j)
    print(total)
