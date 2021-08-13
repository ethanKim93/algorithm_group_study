
# 빈 리스트 만들어서 교환


def rev(i) :
    N = len(i)
    li = list(i)
    for k in range(N//2):
        li[k] , li[N-1-k] = li[N-1-k], li[k]
    return ''.join(map(str, li))


def rev_2(i) :
    N = len(i)
    li = list(i)
    for k in range(N//2):
        tmp = li[k]
        li[k] = li[N-1-k]
        li[N-1-k] = tmp
    return ''.join(map(str, li))

# 빈 문자열 만들어서 뒤에서 부터 읽어오기


def rev_1(i) :
    ni = ''
    nN = len(i)
    for k in range(nN):
        ni += i[nN-1-k]
    return ni


print(rev('avs'))
print(rev_1('abs'))
print(rev_2('avs'))