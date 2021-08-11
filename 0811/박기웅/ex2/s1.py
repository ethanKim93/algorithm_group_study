import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    set_a = list(map(int, input().split()))
    n = len(set_a)
    bflag = 0 #부분집합 중 합이 0 이되는 부분집합이 있으면 1, 없으면 0
    for i in range(1<<n): #비트연산을 통한 부분집합 생성
        part = []
        for j in range(n):
            if i & (1<<j): #i의 j번째 비트 검사하여 있는 경우,
                part.append(set_a[j]) #부분집합의 원소 추가

        if part: #공집합 제외
            part_sum = 0
            for p in part:
                part_sum += p
            if not part_sum: # part_sum = 0 인 경우 존재하면
                bflag = 1    # bflag= 1로 만들어 주고 for 문에서 나간 다음
                break

        if bflag: #큰 for문에서도 나감
            break
    print('#{} {}'.format(tc, bflag))




