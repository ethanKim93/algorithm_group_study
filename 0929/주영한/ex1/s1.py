number = "0000000111100000011000000111100110000110000111100111100111111001100111"

length = len(number)
print(length)
for i in range(length//7):
    temp_str = number[7 * i : 7 * i + 7]
    temp_num = 0
    for j in range(7):
        if temp_str[6 - j] == '1':
            temp_num += 2 ** j
    print(temp_num, end=" ")