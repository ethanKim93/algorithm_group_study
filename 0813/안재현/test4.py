def atoi(string):
    total = 0
    for i in range(len(string)):
        total *= 10
        total += ord(string[i]) - 48
    return total


def itoa(nums):
    li = []
    while nums > 0:
        num = nums % 10
        li.insert(0, chr(num + 48))
        nums = nums // 10
    strings = "".join(li)
    return strings


print(atoi("1234567890"))
print(type(atoi("1234567890")))

st = ""
print(itoa(1234567890))
print(type(itoa(1234567890)))