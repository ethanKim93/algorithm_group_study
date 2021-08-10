import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    # 버블소트를 이용해 정렬을 해서
    for end in range(len(a)-1, 0, -1):
        for i in range(0, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]

    result = a[-1] - a[0]   # 정렬된 리스트의 가장 마지막 값에서 앞의 값을 빼면

    print('#{} {}'.format(tc, result))
