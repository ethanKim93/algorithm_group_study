import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T+1):
    str1 = input().rstrip()
    str2 = input().rstrip()

    str1_dict = dict()

    # str1의 각 알파벳을 key로 하는 dict 생성
    for alphabet in str1:
        str1_dict[alphabet] = 0

    # str2를 순회하면서 str1의 key에 str2의 알파벳이 있다면 str1_dict의 value +1
    for alphabet in str2:
        if alphabet in str1_dict.keys():
            str1_dict[alphabet] += 1

    # 가장 많은 글자의 갯수는?
    result = 0
    for alphabet in str1_dict.values():
        if result < alphabet:
            result = alphabet

    print('#{} {}'.format(test_case, result))

