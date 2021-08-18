import sys

sys.stdin = open('sample_input.txt', 'rt', encoding='UTF8')

T = int(input())

for i in range(0, T):
    N = input()
    M = input()
    my_dict = {}
    result = 0
    for j in N:     # N 문자열을 글자별로 나누어 딕셔너리에 담는다
        my_dict[j] = 0

    for key, values in my_dict.items():
        for a in range(len(M)):  # M 문자열의 글자를 1개씩 my_dict의 key값과 비교한다.
            if key == M[a]:   # 동일할 경우 해당 key의 value값에 1을 더한다.
                my_dict[key] += 1
                for val in my_dict.values():    # value값 중 최댓값을 result에 저장.
                    if my_dict[key] > result:
                        result = my_dict[key]
    print('#{} {}'.format(i+1, result))