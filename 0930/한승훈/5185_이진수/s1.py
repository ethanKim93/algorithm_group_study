import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, nums = input().split()
    ans = ''
    bit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(int(N)):
        num = nums[i]
        for j in range(3, -1, -1):
            idx = bit.index(num)
            if idx//(2**j):
                ans += '1'
                if idx >= 2**j:
                    num = bit[idx-2**j]
                else:
                    num = '0'
            else:
                ans += '0'
    print('#{} {}'.format(tc,ans))