import sys
sys.stdin = open("sample_input.txt")

password = {
    "0001101": "0",
    "0011001": "1",
    "0010011": "2",
    "0111101": "3",
    "0100011": "4",
    "0110001": "5",
    "0101111": "6",
    "0111011": "7",
    "0110111": "8",
    "0001011": "9",
}

for case in range(int(input())):
    N, M = map(int, input().split())

    st = [input() for _ in range(N)]

    lines = set()
    for row in st:
        for col in range(M-1, -1, -1):
            if row[col] != "0":
                lines.add(row)
                break

    total = 0

    # print(lines)

    bits = []

    while lines:
        line = lines.pop()

        bits_list = []
        for i in line:
            asc = ord(i)
            integer = asc - 48 if asc <= 57 else asc - 55
            for j in range(4):
                bits_list.append(str(integer >> (3 - j) & 1))

        bits.append(''.join(bits_list))

    # print(bits)

    keys = set()

    for bit in bits:
        end = M * 4
        while end:
            end -= 1
            if bit[end] != "0":
                mul = 1
                while True:
                    try:
                        nums = []
                        for i in range(end, end - (7 * mul) * 8, 7 * (-mul)):
                            key = []
                            for j in range(i, i - (7 * mul), -mul):
                                key.append(str(bit[j]))
                            key.reverse()
                            nums.append(password[''.join(key)])
                        if ''.join(nums) not in keys:
                            code = 0
                            for p in range(8):
                                if p % 2:
                                    code += int(nums[p]) * 3
                                else:
                                    code += int(nums[p])
                            if code % 10 == 0:
                                for p in range(8):
                                    total += int(nums[p])
                                keys.add(''.join(nums))
                        end -= 7 * mul * 8
                        break
                    except KeyError:
                        mul += 1

    print("#{} {}".format(case + 1, total))
