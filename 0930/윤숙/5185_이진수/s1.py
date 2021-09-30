import sys
sys.stdin=open('input.txt')
HEXDIC = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
          "D": 13, "E": 14, "F": 15}
T=int(input())
for tc in range(1,T+1):
    p = []
    hexlen,hexarr=map(str,input().split())

    for i in range(int(hexlen)-1,-1,-1):
        tmp=hexarr[i]
        DEXNUM=HEXDIC.get(tmp)

        for j in range(0,4):
           if (DEXNUM &(1<<j)):
               p.append(1)
           else:
               p.append(0)

    print('#{} '.format(tc), end='')
    for i in range(len(p)-1,-1,-1):
        print(p[i], end='')
    print()

