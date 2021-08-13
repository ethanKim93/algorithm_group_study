import sys
sys.stdin = open('input.txt')

T = int(input())
for tec in range(1, T+1):
    tc, tcnum = input().split()
    text = list(map(str, input().split()))
    box = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cntbox = [0]*10
    check = -1
    newbox = []
    for b in box:
        check += 1
        for t in text:
            if b == t:
                cntbox[check] += 1
    check = 0
    for cnt in box:
        newbox.append((cnt+' ') * cntbox[check])
        check += 1

    newbox2 = ' '.join(newbox)

    print('{}'.format(tc))
    print('{}'.format(newbox2))