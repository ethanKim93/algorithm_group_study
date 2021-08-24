import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    case, N = map(str, input().split())
    N= int(N)
    input_yeol = list(input().split())
    yeol = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    print('{}'.format(case))
    for i in range(10):
        j=0
        while j < N:
            if yeol[i]==input_yeol[j]:
                print(yeol[i],end =' ')
            j += 1
    print()
        
    
    

