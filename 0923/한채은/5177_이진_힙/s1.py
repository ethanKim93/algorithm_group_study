import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))

    for i in range(2, N+1):
        # 부모가 자식노드보다 크면 자리 바꿔주기
        while numbers[i] < numbers[i//2]:
            numbers[i], numbers[i//2] = numbers[i//2], numbers[i]
            # i도 같이 //2 해줘야함!! 중요
            i = i//2

    ans = 0
    while N//2 != 0:
        ans += numbers[N//2]
        N = N//2
    print('#{} {}'.format(tc, ans))