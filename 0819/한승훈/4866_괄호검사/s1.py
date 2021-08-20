import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    words = input()
    br1 = ['(', '{']
    br2 = [')', '}']
    cnt = 1
    br_word = []
    for word in words:
        if word in br1:
            br_word.append(word)  # 괄호들 모두 삽입
        elif word in br2:
            if not len(br_word):  # br_word에 넣은것이 없다면
                cnt = 0
                break
            br = br_word.pop()
            if br == '{' and word == '}':
                continue
            elif br == '(' and word == ')':
                continue
            else:
                cnt = 0
                break
    if len(br_word):  # 남아 있는것이 있는지 확인
        cnt = 0
    print('#{} {}'.format(tc, cnt))




