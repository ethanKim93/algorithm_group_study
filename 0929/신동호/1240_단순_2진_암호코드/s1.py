import sys
sys.stdin = open('input.txt')

pattern = [0b0001101, 0b0011001, 0b0010011, 0b0111101, 0b0100011, 0b0110001, 0b0101111, 0b0111011, 0b0110111, 0b0001011]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    tot = 0
    result = 0
    code = []
    for _ in range(N):
        nums = input()
        i = M-1
        while not i < 0 and not code:
            if int(nums[i]):
                for j in range(8):
                    for p in range(len(pattern)):
                        if not pattern[p] ^ int(nums[i-7*j-6:i-7*j+1], 2):
                            code += [p]
                break
            i -= 1

    for k in range(8):
        result += code[k]
        if k & 1:
            tot += 3 * code[k]
        else:
            tot +=  code[k]

    if tot%10:
        result = 0
    print("#{} {}".format(tc, result))