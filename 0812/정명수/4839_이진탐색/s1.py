import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1,T+1):
    P, A, B = map(int, input().split())
    AL, BL = 1, 1
    AR, BR = P, P
    A_find, B_find = 0, 0
    while 1:
        AP = int(int(AL+AR)/2)
        BP = int(int(BL+BR)/2)
        if AP < A:
            AL = AP
        elif A < AP:
            AR = AP
        else:
            A_find = 1
        if BP < B:
            BL = BP
        elif B < BP:
            BR = BP
        else:
            B_find = 1
        if A_find == 1 or B_find == 1:
            if A_find > B_find:
                print('#{} A'.format(test_case))

            elif A_find < B_find:
                print('#{} B'.format(test_case))

            else:
                print('#{} 0'.format(test_case))
            break