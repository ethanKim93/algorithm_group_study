# 0DEC

pattern = [0b001101, 0b010011, 0b111011, 0b110001, 0b100011, 0b110111, 0b001011, 0b111101, 0b011001, 0b101111]



num = list(input())

output = ""
for n in num:
    n16 = int(n, 16)
    for i in range(3, -1, -1):
        output += '1' if n16 & (1 << i) else '0'


i = len(output)
while not i < 6:
    if int(output[i-1]):
        for p in pattern:
            if not p ^ int(output[i-6:i], 2):
                print(p, end=', ')
                i -= 6
                break
    else:
        i -= 1