import sys
sys.stdin = open('sample_input.txt')

def merge_sort(m):                  # 분할
    if len(m) == 1:                 # list m이 더이상 분할할 수 없을 때
        return m

    middle = len(m)//2              # 좌,우로 나눌 지점

    m_l = merge_sort(m[:middle])
    m_r = merge_sort(m[middle:])

    return merge(m_l,m_r)           # 합병해서 리턴

def merge(l,r):                     # 합병
    global cnt
    if l[-1] > r[-1]:               # 왼쪽 마지막 숫자가 오른쪽 마지막 숫자보다 클때 카운트
        cnt += 1
    size_l = len(l)                 # 왼쪽배열의 크기
    size_r = len(r)                 # 오른쪽배열의 크기
    result = [0] * (size_l + size_r)            # 시간 단축을 위해 미리 배열을 만들어두고 값을 입력 (append,pop 안쓰기위해서)
    idx_l = idx_r = 0               # l,r의 인덱스 변수
    i = 0                           # result의 인덱스 변수
    while idx_l < size_l or idx_r < size_r:     # 인덱스가 유효할 때 오름차순 정렬 (미리만들어둔 result 배열에 입력 후 반환)
        temp = 0
        if idx_l < size_l and idx_r < size_r:   # 좌,우 모두 존재할 때
            if l[idx_l] <= r[idx_r]:    # 왼쪽의 현재인덱스의 value가 오른쪽보다 작거나 같을때
                temp = l[idx_l]     # 임시변수에 value 저장
                idx_l += 1          # 인덱스 갱신
            else:                   # 오른쪽의 현재 인덱스의 value가 왼쪽보다 작을때
                temp = r[idx_r]
                idx_r += 1
        elif idx_l < size_l:        # 왼쪽만 존재할 때
            temp = l[idx_l]
            idx_l += 1
        elif idx_r < size_r:        # 오른쪽만 존재할 때
            temp = r[idx_r]
            idx_r += 1
        result[i] = temp            # 결과 배열에 정렬결과 저장
        i += 1                      # 인덱스 갱신
    return result

for tc in range(1, int(input())+1):
    N = int(input())                            # 정수의 개수
    nums = list(map(int, input().split()))      # 정렬할 정수 리스트
    cnt = 0                                     # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우를 세기 위한 변수
    print('#{} {} {}'.format(tc, merge_sort(nums)[N//2], cnt))