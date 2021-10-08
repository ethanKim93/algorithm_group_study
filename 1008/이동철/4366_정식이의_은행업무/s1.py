import sys
sys.stdin = open('sample_input.txt', 'r')


# 완전 탐색으로 문제를 해결하였다. 다루기 편하도록 모두 str 형식으로 받아와 나눠서 사용할 수 있도록 하였고
# 마지막에는 int를 통해 2진법, 3진법을 10진수로 변환하여 비교하였다.
# 대략적인 방법을 좀더 자세히 설명하자면 예시 테스트 케이스를 바탕으로 설명하겠다.
# 이진법 1010을 가지고 가능한 모든 경우의 수를 따지면
# 첫번째 자리가 0,1 두번째 자리 0,1 세번째 자리 0,1 네번째 자리 0,1 로 총 8가지이다.
# 그래서 반복문을 길이 *2만큼 반복시키며
# 각 자리의 인덱스는 첫번째 자리 인덱스 0,1 두번쨰 자리 인덱스 2,3 세번째 자리 인덱스 4,5 네번째 자리 인덱스 6,7이 된다.
# 이것은 바꿔 말하면 반복 숫자 i 를 2진법의 수인 2로 나눈 몫이 되고 이에 할당되는 값은 0과 1이기에 값은 나머지가 된다.
# 따라서 길이 *2 만큼 반복하며 각 자리별로 0,1을 할당해주면 끝

T = int(input())
for tc in range(1, T + 1):
    binary = list(input())
    ternary = list(input())
    # 다루기 편하도록 모두 str 형식으로 받아오기

    check = 0  # 이중 for문 탈출 parameter
    for i in range(len(binary) * 2):  # 이진법 0,1 스위칭 되므로 길이 *2 만큼 반복
        re_binary = binary[:]
        re_binary[i // 2] = str(i % 2)
        a = ''.join(re_binary)
        for j in range(len(ternary) * 3):  # 삼진법 0,1,2 스위칭 길이 *3 만큼 반복
            re_ternary = ternary[:]
            re_ternary[j // 3] = str(j % 3)
            b = ''.join(re_ternary)
            if int(a, 2) == int(b, 3):
                # int 를 통해 2진법, 3진법을 10진수로 변환
                print('#{} {}'.format(tc, int(a, 2)))
                check = 1
                break
        if check == 1:
            break
