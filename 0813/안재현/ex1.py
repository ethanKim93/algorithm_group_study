a = '12345'
b = ''
List_a = list(a)
for i in range(len(a)):
    b += List_a[len(a) - i - 1]
print(b)