import sys

sys.stdin = open('input.txt')
T = int(input())
dic_N = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
for tc in range(1, T + 1):
    TN, LN = input().split()
    NUMList = list(input().split())
    arr_N = []
    arr_RN=[]
    Sum_Arr=[0]*10
    for i in range(int(LN)):
        for K, V in dic_N.items():
            if NUMList[i] == K:
                arr_N.append(V)

    for i in range(len(arr_N)):
        Sum_Arr[arr_N[i]]+=1

   
    i=-1
    for k in dic_N:
        i=i+1
        for a in range(Sum_Arr[i]):
            arr_RN.append(k)




    result=' '.join(arr_RN)

    print('#{}'.format(tc))
    print('{}'.format(result))
