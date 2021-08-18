import sys
sys.stdin = open("input.txt")


def func(num):
    if num > 0:
        li = func(num - 1)
        if num % 2 == 0:
            li.append(li[-1] * 2)
        for i in range((num - 1) // 2, 0, -1):
            li[i] += li[i - 1]
        print(*(li + li[(num-1)//2::-1]))
        return li
    else:
        print(1)
        return [1]


for case in range(int(input())):
    print("#{}".format(case + 1))
    func(int(input()) - 1)
