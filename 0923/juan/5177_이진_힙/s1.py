import sys
sys.stdin = open('sample_input.txt')


T = int(input())


def heap(i):                                        # 이진 최소힙 함수
    while i//2 and tree[i//2] > tree[i]:            # 루트 노드 번호에 도달하지 않았고 부모 노드의 값이 자식 노드의 값보다 크면 반복
        tree[i//2], tree[i] = tree[i], tree[i//2]   # 부모 노드의 값과 자식 노드의 값을 교환
        i //= 2                                     # 부모 노드의 위치에서 다시 최소힙 여부 확인을 위해 i값 갱신


for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    nums = list(map(int, input().split()))
    total = 0

    for idx, num in enumerate(nums, start=1):
        tree[idx] = num                             # 입력된 숫자를 tree 배열의 idx번 인덱스에 할당
        heap(idx)                                   # 이진 최소힙 함수 호출

    while N:
        total += tree[N//2]                         # N번 노드의 조상 노드들의 값을 루트 노드에 도달할때까지 total변수에 합산
        N //= 2
    print('#{} {}'.format(tc, total))