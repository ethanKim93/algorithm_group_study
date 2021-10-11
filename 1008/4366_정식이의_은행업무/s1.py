import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def func():
    global THR
    two = 0
    for i in range(len(TWO)): # int 2 써도 되지만 한 번 해봄
        two +=  TWO[i] * 2 ** (len(TWO)-i-1)

    cand = set()
    for i in range(len(TWO)):
        cand.add(two ^ (1<<i))

    
    for i in range(len(THR)):
        for t in range(3):
            if THR[i] != t:
                tmp = THR[i]
                THR[i] = t
                three = 0
                for j in range(len(THR)):
                    three += THR[j] * 3 ** (len(THR)-j-1)
                if three in cand:
                    print('#{} {}'.format(tc, three))
                    return
                THR[i] = tmp


for tc in range(1, T+1):
    TWO = list(map(int, list(input())))
    THR = list(map(int, list(input())))
    func()



