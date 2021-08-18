import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    A, B = input().split()
    i = cnt = 0
    la = len(A)
    lb = len(B)
    while(i < la-lb+1):
        if A[i:i+lb] == B:
            cnt += 1
            i += lb # 문자가 일치하면 다음 인덱스로 넘어감
        else:
            i += 1 # 문자 불일치시 한 칸 뒤 인덱스로
    ans = (la - lb*cnt) + cnt # (A의 길이 - B의 길이 * 일치한 숫자의 개수) + 일치한 숫자의 개수
    print('#{} {}'.format(tc, ans))



