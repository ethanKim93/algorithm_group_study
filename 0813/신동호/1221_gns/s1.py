import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
alien_n = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN'] # 외계 수 케이스
# 무지성 brute force
for tc in range(1, T+1):
    K, N = input().split()
    N = int(N)
    sent = input()
    cnt_box = [0] * 10 # 카운팅 정렬
    print(K) # 입력값 그대로 써먹기
    for ind in range(10): # 모든 외계 수 조사
        i = 0
        j = 0
        while i < len(sent): #1213 코드와 유사
            if alien_n[ind][j] != sent[i]:
                i = i - j
                j = -1
            if j == len(alien_n[ind]) - 1:
                cnt_box[ind] += 1
                i = i - j
                j = -1
            i += 1
            j += 1
        print(' '.join([alien_n[ind]] * cnt_box[ind]), end = ' ') #띄어쓰기 있도록 붙여줌
    print()