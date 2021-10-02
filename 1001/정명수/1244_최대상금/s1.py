import sys
sys.stdin = open('input.txt')

def change_num(N):
    number = 0
    for i in range(len(N)-1,-1,-1):
        number += int(N[i])*(10**(len(N)-1-i))
    return number

def change(N,r):
    global max_num
    if r == counter:
        number1 = change_num(N)
        if max_num < number1:
            max_num = number1
        return
    if r >= len(N)-2:
        N[len(N)-1],N[len(N)-2] = N[len(N)-2],N[len(N)-1]
        change(N,r+1)
    else:
        for i in range(r,len(N)-1):
            for j in range(i+1,len(N)): # (0,1) (0,2) (1,2)
                if max(N[i:]) == N[j]:
                    N[i], N[j] = N[j], N[i] # N = 213  321   132
                    change(N,r+1)
                    N[i], N[j] = N[j], N[i]  # N = 123  123   123
                if max(N[i:]) == N[i]:
                    if len(N)!=len(set(N)):
                        change(N,r+1)
                    N[len(N) - 1], N[len(N) - 2] = N[len(N) - 2], N[len(N) - 1]
                    change(N, r + 1)
                    N[len(N) - 1], N[len(N) - 2] = N[len(N) - 2], N[len(N) - 1]

T = int(input())
for tc in range(1,T+1):
    num, counter = input().split()
    max_num = 0
    num = list(num)
    counter = int(counter)
    if len(num) == 2:
        if counter%2:
            num[1], num[0] = num[0], num[1]
            max_num = change_num(num)
        else:
            max_num = change_num(num)
    else:
        change(num, 0)
    print('#{} {}'.format(tc,max_num))
