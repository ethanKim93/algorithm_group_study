#5356. 의석이의 세로로 말해요
T = int(input())
for tc in range(1,T+1):
    word = [list(input()) for _ in range(5)]
    mw = 15

    for w in word:
        if mw <= len(w):
            mw = len(w)
    for w in word:
        while len(w) < mw:
            w.append('*')

    # if len(w) < mw:
        # w += (mw-len(w))*'*'

    ans = ''
    for i in range(mw):
        for j in range(5):
            ans += word[j][i]
    print('#{} {}'.format(tc, ans.replace('*',"")))

    #풀이 1. 문제 내 최대문자길이인 15만큼 모든 리스트를 맞추고 제거
    #풀이 2. 최대문자길이 구하는 for, 구한 최대문자길이에 맞게 리스트글자수 맞추는 for