password = {
    "001101": 0,
    "010011": 1,
    "111011": 2,
    "110001": 3,
    "100011": 4,
    "110111": 5,
    "001011": 6,
    "111101": 7,
    "011001": 8,
    "101111": 9,
}

st = "0DEC"

bits_list = []
for i in st:
    asc = ord(i)
    integer = asc - 48 if asc <= 57 else asc - 55
    for j in range(4):
        bits_list.append(str(integer >> (3 - j) & 1))

bits = ''.join(bits_list)

front = 0
while front < len(bits):
    key = bits[front:front + 6]
    if key in password.keys():
        print(password[key])
        front += 6
    else:
        front += 1
