import sys

sys.stdin = open('input.txt')
T = int(input())
dic_N = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
for tc in range(1, T + 1):
    TN, LN = input().split()
    NUMList = list(input().split())
    arr_N = []
    arr_RN=[]
    for i in range(int(LN)):
        for K, V in dic_N.items():
            if NUMList[i] == K:
                arr_N.append(V)

    for i in range(0,len(arr_N)-1):
        min=i
        for j in range(i+1, len(arr_N)):
            if arr_N[min]>arr_N[j]:
                min=j

            arr_N[i],arr_N[min]=arr_N[min],arr_N[i]

    for i in range(len(arr_N)):
        for K, V in dic_N.items():
            if arr_N[i] == V:
                arr_RN.append(K)


    result=' '.join(arr_RN)

    print('#{}'.format(tc))
    print('{}'.format(result))
