import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    twoNum = input()
    threeNum = input()

    anslist = []


    for idx,i in enumerate(twoNum):
        if i == '1':
            temp = int(twoNum[:idx]+'0'+twoNum[idx+1:],2)
        else:
            temp = int(twoNum[:idx] + '1' + twoNum[idx + 1:], 2)
        anslist.append(temp)

    ans = 0
    for idx, i in enumerate(threeNum):
        if i == '0':
            temp1 = int(threeNum[:idx] + '1' + threeNum[idx + 1:], 3)
            temp2 = int(threeNum[:idx] + '2' + threeNum[idx + 1:], 3)
        elif i == '1':
            temp1 = int(threeNum[:idx] + '0' + threeNum[idx + 1:], 3)
            temp2 = int(threeNum[:idx] + '2' + threeNum[idx + 1:], 3)
        elif i == '2':
            temp1 = int(threeNum[:idx] + '0' + threeNum[idx + 1:], 3)
            temp2 = int(threeNum[:idx] + '1' + threeNum[idx + 1:], 3)
        if temp1 in anslist:
            ans = temp1
            break
        if temp2 in anslist:
            ans = temp2
            break

    print('#{} {}'.format(tc,ans))