import sys
sys.stdin = open('test_input.txt', 'rt', encoding='UTF8')

for i in range(10):
    t = int(input())
    patt = input()
    senten = input()

    cnt = 0
    for i in range(len(senten) - len(patt) + 1):
        if senten[i:i + len(patt)] == patt:
            cnt += 1

    print('#{} {}'.format(t, cnt))

#
#     #1차원 배열
#     cunt = 0  # 겹쳐지는 게 있으면 카운트 수를 하나씩 증가해줘야하니 설정값 세팅
#     for i in range(len(p)-s+):
#         p[i:i+2] = s
#
#
# 1.#p의 문자열 수를 구하고, 그걸 반복문으로 돌려서 하나하나 검사
# 2.
# import sys
# sys.stdin = open('input.txt', 'rt', encoding='UTF8')
#
# for tc in range(1, 11):
#     N = int(input())
#     text = input()
#     texts = input()
#
#     cnt = 0
#     for i in range(0, len(texts)-1):
#         if texts[i] == text[0]:
#             if texts[i:i+len(text)] == text:
#                 cnt += 1
#     print('#{} {}'.format(tc, cnt))