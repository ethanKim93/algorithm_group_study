s = '12345'


def reverse(a):
    b = ''
    List_a = list(a)
    for i in range(len(a)):
        b += List_a[len(a) - i - 1]
    return b


print(s)
print(reverse(s))
