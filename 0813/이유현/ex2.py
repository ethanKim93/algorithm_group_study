# # 숫자를 문자로 바꾸기
# num = int(input())
# strnum = '{}'.format(num)
#
# print(strnum)
# print(type(strnum))

# 문자를 숫자로 바꾸기
strnum = input()
digit = len(strnum)

while True:
    i = 0
    atoi = 0
    if ord(strnum[i]) == 45:
        for j in range(1, digit):
            atoi += (ord(strnum[j]) - 48) * (10 ** (digit - j - 1))
        print(atoi * (-1))
        break

    else:
        for k in range(digit):
            atoi += (ord(strnum[k]) - 48) * (10 ** (digit - k - 1))
        print(atoi)
        break


