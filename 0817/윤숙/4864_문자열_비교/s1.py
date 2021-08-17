import sys

sys.stdin = open('input.txt', encoding='utf8')
T = int(input())
def strfinder (S1, S2, S1L,S2L):
    i = 0
    j = 0
    while j < S1_Len and i < S2_Len:
        if S2[i] != S1[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == S1_Len:
        return 1
    else:
        return 0

for tc in range(1, T + 1):
    S1 = input()
    S2 = input()
    S1_Len = len(S1)
    S2_Len = len(S2)

    print('#{} {}'.format(tc,strfinder(S1,S2,S1_Len,S2_Len)))


