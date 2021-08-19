import sys
sys.stdin = open("input.txt")

for case in range(int(input())):
    li = [1]
    print("#{}".format(case + 1))
    for i in range(int(input())):
        if i > 1:
            if not i % 2:
                li.append(li[-1] * 2)
            for j in range((i - 1) // 2, 0, -1):
                li[j] += li[j - 1]

        print(*(li + li[(i - 1) // 2::-1] if i > 0 else li))