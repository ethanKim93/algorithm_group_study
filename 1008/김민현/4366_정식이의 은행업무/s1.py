#런타임 오류 발생
import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    twoNum = input()
    threeNum = input()

    twoN = len(twoNum)
    twolist = []
    threeN = len(threeNum)
    anslist = []

    for j in range(twoN):
        temp = 0
        for idx,i in enumerate(twoNum):
            if j == idx:
                if not int(i):
                    temp += 2 ** (twoN - 1 - idx)
            else:
                temp += int(i)*2**(twoN-1-idx)
        twolist.append(temp)

    twomax = max(twolist)
    flag = 0
    j = 0
    while j < threeN:
        temp = 0
        for idx,i in enumerate(threeNum):
            if j == idx:
                if i == '0':
                    temp += 3 ** (threeN - 1 - idx)
                elif i == '1':
                    if flag:
                        temp += 2*3 ** (threeN - 1 - idx)
                        flag = 0
                    else:
                        j -= 1
                        flag = 1
                elif i == '2':
                    temp += 3 ** (threeN - 1 - idx)
            else:
                temp += int(i)*3**(threeN-1-idx)
            if twomax < temp:
                break
        if temp in twolist:
            anslist.append(temp)
            break
        j += 1

    print('#{} {}'.format(tc,*anslist))