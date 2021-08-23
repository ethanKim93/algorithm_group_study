import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    text = [list(input()) for _ in range(5)]
    print('#{} '.format(tc), end='')
    for i in range(15):
        for j in range(5):
            try:
                print(text[j][i], end='')
            except:
                pass
    print()