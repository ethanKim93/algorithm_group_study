a = '12345'
b = ''
List_a = list(a)
for i in range(len(a)):
    b += List_a[len(a) - i - 1]
print(b)


def change_str(x):
    return '{}'.format(x)


neg = -1
print(change_str(a))
print(type(change_str(a)))
print(change_str(neg))
print(type(change_str(neg)))
