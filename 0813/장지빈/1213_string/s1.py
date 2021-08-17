import sys
sys.stdin = open('test_input.txt')

for tc in range(10):
    T = input()
    p = input()
    t = input()
    cnt = 0
    for i in range(len(t)-len(p)+1):
        if t[i:i+len(p)] == p:
            cnt += 1
    print('#{} {}'.format(T, cnt))