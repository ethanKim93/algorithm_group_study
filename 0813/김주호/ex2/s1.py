def itoa(string):
    total = 0
    for i in range(len(string)):
        total *= 10
        total += ord(string[i]) - 48
    return total


print(itoa("1234567890"))
