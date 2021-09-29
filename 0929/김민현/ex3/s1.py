import sys
sys.stdin = open('input.txt')

T = int(input())

pattern = [
    '001101',
    '010011',
    '111011',
    '110001',
    '100011',
    '110111',
    '001011',
    '111101',
    '011001',
    '101111'
]

for tc in range(T):
    data = input()
    bit = ''
    for i in data:
        for j in range(3,-1,-1):
            bit += "1" if int(i,16) & (1<<j) else "0"
    print(bit)
    ans = ''
    k = len(bit)-1
    while k > 5:
        if bit[k] == '1':
            for f in range(len(pattern)):
                if bit[k-5:k+1] == pattern[f]:
                    ans += str(f)
                    k -= 5
        k -= 1
    print(','.join(ans[::-1]))
