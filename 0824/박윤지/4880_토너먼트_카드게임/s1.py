import sys
sys.stdin = open('sample_input.txt')

def battle(li):
    if len(li) == 2:
        a = li[0][1]
        b = li[1][1]
        if (a, b) in [(1, 3), (2, 1), (3, 2)]:
            return li[0]
        elif (a, b) in [(1, 2), (2, 3), (3, 1)]:
            return li[1]
        else:  # 비겼을 때
            return li[0]

def do_split(li):
    global list21
    if len(li) > 2:
        left_end = (0 + len(li) -1) // 2
        new_list1 = li[0: left_end + 1]
        new_list2 = li[left_end + 1:]
        do_split(new_list1)
        do_split(new_list2)
    elif len(li) == 2:
        list21.append(battle(li))
    elif len(li) == 1:
        list21.append(li[0])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))  # 가위바위보 카드 번호 / 1번은 인덱스 0
    new_card = []
    for idx, val in enumerate(card):
        new_card.append((idx+1, val))
    list21 = []
    do_split(new_card)
    while len(list21) > 1:
        new_card = list21
        list21 = []
        do_split(new_card)
    print('#{} {}'.format(tc, list21[0][0]))


# 승자의 카드 출력
# import sys
# sys.stdin = open('sample_input.txt')
#
# def battle(li):
#     if len(li) == 2:
#         a = li[0]
#         b = li[1]
#         if (a, b) in [(1, 3), (2, 1), (3, 2)]:
#             return a
#         elif (a, b) in [(1, 2), (2, 3), (3, 1)]:
#             return b
#         else:  # 비겼을 때
#             return a
#
# def do_split(li):
#     global list21
#     if len(li) > 2:
#         left_end = (0 + len(li) -1) // 2
#         new_list1 = li[0: left_end + 1]
#         new_list2 = li[left_end + 1:]
#         do_split(new_list1)
#         do_split(new_list2)
#     elif len(li) == 2:
#         list21.append(battle(li))
#     elif len(li) == 1:
#         list21.append(li[0])
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     card = list(map(int, input().split()))  # 가위바위보 카드 번호 / 1번은 인덱스 0
#     student = list(range(1, len(card)+1))  # 학생 번호 / 인덱스 0번이 1번
#     list21 = []
#     do_split(card)
#     while len(list21) > 1:
#         card = list21
#         list21 = []
#         do_split(card)
#     print(list21)



