#미구현

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def combine(choice):
    global a_list
    global b_list
    if choice == 0:
        for j in food:
            if j not in a_list:
                b_list.append(j)
        print('a',a_list)
        print('b',b_list)
        b_list = []
        return

    for i in food:
        a_list.append(i)
        combine(choice-1)
        a_list.pop(-1)


for tc in range(1,T+1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    b_list = []
    a_list = []
    food = [i for i in range(N)]

    combine(N/2)
    ans = 0
    #print('#{} {}'.format(tc,ans))