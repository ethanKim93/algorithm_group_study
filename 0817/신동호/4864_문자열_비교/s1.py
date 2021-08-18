# import sys
# sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    i = j = result = 0
    while i < len(str2):
        if str1[j] != str2[i]:
            i -= j
            j = -1
        i += 1
        j += 1
        if j == len(str1):
            result = 1
            break
    print('#{} {}'.format(tc,result))
    # 보이어무어 실패
    # letters = {}
    # i = j = len(str1)-1
    # result = 0
    # for let in range(len(str1)):
    #     letters[str1[let]] = len(str1) - let - 1
    # while i <= len(str2) - len(str1) and j <= len(str1) - 1:
    #     print(i,j)
    #     if str2[i] != str1[j]:
    #         i += letters.get(str1[j], len(letters))
    #         print(letters.get(str1[j], len(letters)))
    #         j += 1
    #     if j==0:
    #         result = 1
    #         break
    #     i -= 1
    #     j -= 1
    # print(result)
