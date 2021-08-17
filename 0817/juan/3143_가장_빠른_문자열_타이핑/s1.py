T = int(input())

for tc in range(1, T+1):
    A,B = input().split()

    idx = cnt = 0                       # 보고있는 idx, 타이핑 횟수 cnt 초기화
    while idx < len(A):                 # idx 가 A의 길이를 넘지 않는 경우
        if A[idx:idx+len(B)] == B:      # 해당 idx부터 B의 길이만큼 slicing해서 B와 일치여부 확인
            idx += len(B)               # 일치하면 idx를 B의 길이만큼 증가
        else:
            idx += 1                    # 불일치하면 idx 1 증가
        cnt += 1                        # 어떤 경우든 타이핑 횟수 1 증가
    print('#{} {}'.format(tc, cnt))