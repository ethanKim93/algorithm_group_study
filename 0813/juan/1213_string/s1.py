import sys
sys.stdin = open('test_input.txt')

for _ in range(1, 11):
    tc = input()
    target = input()
    pattern = input()
    result = 0

    for i in range(len(pattern)-len(target)+1):
        if pattern[i:i+len(target)] == target:
            result += 1

    print('#{} {}'.format(tc, result))