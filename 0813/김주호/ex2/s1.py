def atoi(string):
    total = 0
    for i in range(len(string)):
        total *= 10
        total += ord(string[i]) - 48
    return total


def itoa(nums, string):
    li = []
    while nums > 0:
        num = nums % 10
        li.insert(0, chr(num + 48))
        nums = nums // 10
    string = "".join(li)
    print(string)


print(atoi("1234567890"))

st = ""
itoa(1234567890, st)