import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1,t+1):
    word = input()
    text = input()
    ans = 0
    tl, wl = len(text), len(word) # 문장과 단어의 길이

    for i in range(tl): # 문장을 하나씩 돌면서
        cnt = 0
        for x in range(wl): # 단어와 일치하는지 확인
            if i+x >= tl: # 확인해야하는 단어의 수가 문장의 길이를 벗어나면 break
                break

            elif text[i+x] == word[x]: # 문장과 단어가 같으면 cnt ++1
                cnt += 1

        if cnt == wl: # 단어와 완전 일치하는게 있으면 ans = 1
            ans = 1

    print("#{} {}".format(tc,ans))