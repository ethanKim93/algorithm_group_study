import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for _ in range(1,T+1):
    tc, N = input().split()
    words = list(map(str, input().split()))
    num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    ans = ''
    i = 0
    while i < 10:
        for word in words:
            if num[word] == i:
                ans += word + ' '
        i += 1
    print('{} {}'.format(tc, ans[:-1]))
