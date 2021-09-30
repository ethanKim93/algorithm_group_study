import sys
sys.stdin = open("input.txt")

password = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

for case in range(int(input())):
    N, M = map(int, input().split())

    st = [input() for _ in range(N)]

    line = ""
    for row in st:
        if "1" in row:
            line = row
            break

    code = ""
    for col in range(M-1, -1, -1):
        if line[col] == "1":
            code = line[col-55: col+1]
            break

    nums = []
    for i in range(0, 56, 7):
        nums.append(password[code[i:i+7]])

    if ((nums[0] + nums[2] + nums[4] + nums[6]) * 3 + nums[1] + nums[3] + nums[5] + nums[7]) % 10 == 0:
        print("#{} {}".format(case + 1, sum(nums)))
    else:
        print("#{} {}".format(case + 1, 0))
