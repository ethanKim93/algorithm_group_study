import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    text = input()
    new_text = text[0]
    for i in range(1,len(text)):
        if new_text:
            if new_text[-1] == text[i]:
                new_text = new_text[:-1]
            else:
                new_text += text[i]
        else:
            new_text = text[i]
    print('#{} {}'.format(tc,len(new_text)))

