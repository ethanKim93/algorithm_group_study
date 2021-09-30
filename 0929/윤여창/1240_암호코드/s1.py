import sys
sys.stdin = open("input.txt")

pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for tc in range(int(input())):
    N, M = map(int, input().split())
    code = []
    for _ in range(N):
        inp = input().rstrip('0')
        if inp:
            code.append(inp[len(inp)-56:])
    for co in code:
        num = []
        for i in range(0, len(co), 7):
            num.append(pattern.index(co[i:i+7]))
        if (3*(num[0]+num[2]+num[4]+num[6]) + num[1]+num[3]+num[5] + num[7]) % 10 == 0:
            ans = sum(num)
            break
    else:
        ans = 0
    print('#{} {}'.format(tc+1, ans))