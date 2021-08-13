def atoi(string):
    total = 0
    for i in range(len(string)):
        total *= 10
        total += ord(string[i]) - 48
    return total


def itoa(nums):

    st = ""
    if nums < 0:
        nums *= -1
        st += "-"

    if nums == 0:
        st += "0"
        return st

    li = []
    while nums > 0:
        num = nums % 10
        li.insert(0, chr(num + 48))
        nums = nums // 10

    for i in range(len(li)):
        st += li[i]
    return st


print(atoi("1234567890"))

print(itoa(-1234567890))