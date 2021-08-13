# 정수 -> 문자열


def trans(N):
    li = []
    while N :
        if N < 0 :
            N = -N
        num = N % 10
        li.insert(0,chr(num + 48))
        N //= 10
        N_st = ''.join(map(str,li))
    return N_st


def trans_1(N):
    li = []
    while N :
        if N < 0 :
            N = -N
        num = N % 10
        li.append(chr(num + 48))
        N //= 10
        N_st = ''.join(map(str,li[-1::-1]))
    return N_st


# 문자열 -> 정수

def trans_3(s):
    N_s = []
    num = 0
    l = len(s)
    for i in range(l):
        N_s.append(ord(s[i]) - 48)
    for j in range(l):
        num += N_s[j] * (10**(l-1-j))
    return num


a = trans_3('123')
print(a)
print(type(a))