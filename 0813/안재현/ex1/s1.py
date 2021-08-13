k = '12345'


def reverse1(a):
    s = list(a)
    n = len(s)
    for i in range(n//2):
        s[i], s[n-1-1] = s[n-1-i], s[i]
    return ''.join(map(str, s))

def reverse2(a):
    b = ''
    List_a = list(a)
    for i in range(len(a)):
        b += List_a[len(a) - i - 1]
    return b


print(k)
print(reverse1(k))
print(reverse2(k))
