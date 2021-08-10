import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for a in range(0, T):
    KNM = list(map(int, input().split()))
    M = list(map(int, input().split()))

    print(KNM)
    print(M)
    cnt=0
    energy=KNM[0]
    for i in range(len(M)-1):
        if M[i+1] - M[i] > KNM[0]:
            print('#{} {}'.format(a + 1, 0))
        elif M[i+1] - M[i] < KNM[0]:
            energy -= 1
            cnt += 1
            

