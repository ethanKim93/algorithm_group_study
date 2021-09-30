# 0000000111100000011000000111100110000110000111100111100111111001100111
numbers = list(map(int, input()))

for i in range(len(numbers)//7):
    num = 0
    for j in range(7):
        num += 2 ** j * numbers[7 * (i+1) - j -1]
    if i == len(numbers)//7 - 1:
        print(num)
    else:
        print(num, end=', ')

# import sys
# print(sys.byteorder)