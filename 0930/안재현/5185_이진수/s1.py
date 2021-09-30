import sys
sys.stdin = open('sample_input.txt')

# 16진수의 알파벳만 숫자로 변경시켜줄 dict
Wbit = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

T = int(input())
for tc in range(T):
    N, M = input().split()
    result = ''
    for i in range(len(M)):
        if M[i].isalpha():
            dec = int(Wbit[M[i]])
        else:
            dec = int(M[i])
        Tbit = ''
        for _ in range(4):
            Tbit = str(dec % 2) + Tbit
            dec = dec//2
        result += Tbit
    print("#{} {}".format(tc + 1, result))