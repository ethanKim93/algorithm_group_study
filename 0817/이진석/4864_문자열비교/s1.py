import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    target_word = input()
    string = input()
    status = 0
    for i in range(len(string)-len(target_word)+1):
        if string[i:i+len(target_word)] == target_word:
            status = 1
            break
    print('#{} {}'.format(tc, status))