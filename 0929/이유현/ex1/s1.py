import sys
sys.stdin = open('input.txt')

num = input()
bit_list = []
for i in range(0, len(num), 7):
    bit_list.append(num[i:i+7])

ans = []
for bit in bit_list:
    bit_int = 0
    bit = bit[::-1]
    for b in range(len(bit)):
        if bit[b] == '1':
            bit_int += 2 ** b
    ans.append(bit_int)
print(*ans, end=' ')


