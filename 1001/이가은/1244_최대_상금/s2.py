import sys
sys.stdin = open('input.txt')

def change_num(N):
    number = 0
    for i in range(len(N)-1,-1,-1):
        number += int(N[i])*(10**i)
    return number

def change(N,r):
    global max_num
    if r >= counter:
        number = change_num(N)
        print(number)
        if max_num < number:
            max_num = number
        return
    for i in range(len(N)):
        for j in range(len(N)):
            if i != j:
                N[i], N[j] = N[j], N[i]
                change(N,r+1)
                N[i], N[j] = N[j], N[i]

T = int(input())
for tc in range(1,T+1):
    num, counter = input().split()
    num = list(num)
    counter = int(counter)
    max_num = 0
    change(num,0)
    print(max_num)
