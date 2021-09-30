import sys
sys.stdin = open('sample_input (1).txt')

hexadecimal = {
    '0': 0, '1': 1, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7, '8':8, '9':9, 'A':10, 'B':11,'C':12,'D':13,'E':14,'F':15
}


T = int(input())
for tc in range(1,T+1):
    N, hexa = input().split()
    N = int(N)
    ans = ''
    for i in range(N):
        result = ''
        num = hexadecimal[hexa[i]]
        for j in range(4):
            if num :
                result += str(num % 2)
                num //= 2
            else:
                result += '0'
        ans += result[::-1]
    print('#{} {}'.format(tc,ans))



