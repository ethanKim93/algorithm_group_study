import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    tc = int(input())
    word = input()
    text = input()
    ans = 0

    for i in range(len(text)-len(word)+1):
        for x in range(len(word)):
            if word[x] != text[i+x]: # 같지 않으면 다음 text의 다음 순번으로
                break
        else:
            ans += 1


    print('#{} {}'.format(tc, ans))
