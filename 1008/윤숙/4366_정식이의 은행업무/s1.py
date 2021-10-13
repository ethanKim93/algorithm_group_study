import sys

sys.stdin = open('input.txt')
'''
1
1010(8)8421 1~15까지 표기 가능
212(23)931 1~26까지 표기 가능

'''


# num은 문자열이다.
def convert(num, base):
    tmp = 0
    for n, val in enumerate(list(map(int, num))[::-1]):
        tmp += val * (base ** n)
    return tmp


def check(num, base):
    change_num = convert(num, base)
    for n, val in enumerate(list(map(int, num))[::-1]):
        for j in range(base):
            if val == j:
                continue
            tmp = change_num - val * (base ** n) + j * (base ** n)
            if tmp not in binary:
                binary.append(tmp)
            else:
                return tmp

T = int(input())
for tc in range(1, T + 1):
    bi = input()
    tetra = input()
    binary=[]

    check(bi, 2)

    print('#{} {}'.format(tc,check(tetra, 3)))



