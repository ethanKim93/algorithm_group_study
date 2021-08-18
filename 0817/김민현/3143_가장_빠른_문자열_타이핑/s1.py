import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    A,B = map(str, input().split())
    cnt = 0 # B문자열 길이 만큼
    j = 0
    while j < len(A)-len(B)+1 : #B문자열 길이를 뺀만큼
        flag = True
        for k in range(len(B)):
            if B[k] == A[j+k]:
                  pass
            else:
                 flag = False
                 break
        if flag == True:
            cnt += 1
            j += len(B)
        else :
            j += 1
        flag = True
    print("#{} {}".format(tc, len(A) - cnt * (len(B) - 1)))

