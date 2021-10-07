import sys
sys.stdin = open('sample_input.txt')


def merge(l, r):
    m = []
    l_p, r_p = 0, 0 # 리스트에 값이 존재하는지 여부를 판단하기 위한 변수
    global cnt

    if l[-1] > r[-1]: # 정렬하기 전에 리스트 마지막 숫자가 l가 더 크면
        cnt += 1      # 카운트 +1

# left, right 둘 다 있을 때
    while len(l) > l_p and len(r) > r_p:  # 비교 할 두 값이 모두 있을 때
        if l[l_p] > r[r_p]:              # 왼쪽 값이 클 때는 오른쪽 값이 작다는 뜻이므로 먼저 넣어서 정렬
            m.append(r[r_p])
            r_p += 1
        else:                   # 위와 반대
            m.append(l[l_p])
            l_p += 1

    while len(l) > l_p:  # left 데이터가 없을 때 (정렬해서 남은 큰수)
        m.append(l[l_p])
        l_p += 1

    while len(r) > r_p:  # right 데이터가 없을 때 (정렬해서 남은 큰수)
        m.append(r[r_p])
        r_p += 1

    return m

def part(lis):        # 재귀호출하며 입력받은 리스트를 나누는 절반씩 나누는 함수
    if len(lis) <= 1: # 최대로 나누어져 1개가 되어지면 리턴
        return lis
    half = int(len(lis) // 2)     # half를 절반의 반절의 값으로 하고
    l = part(lis[:half])         #  half를 기준으로 l, r를 나눔
    r = part(lis[half:])
    return merge(l, r)        # 병합함수 호출


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int,input().split()))
    cnt = 0

    ans = part(L)
    #print(ans)
    print('#{} {} {}'.format(tc, ans[N//2], cnt))