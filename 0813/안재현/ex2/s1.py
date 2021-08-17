def change_str(x):
    return '{}'.format(x)


def change_int(x):
    total = 0
    if x[0] == '-':
        for i in range(len(x) - 1):
            total *= 10
            total += ord(x[i + 1]) - 48
        return -total
    else:
        for i in range(len(x)):
            total *= 10
            total += ord(x[i]) - 48
        return total


a = 12345
neg = -1
word = '1234'
neg_word = '-1234'

print(change_str(a))
print(type(change_str(a)))
print(change_str(neg))
print(type(change_str(neg)))

print(change_int(word))
print(type(change_int(word)))
print(change_int(neg_word))
print(type(change_int(neg_word)))