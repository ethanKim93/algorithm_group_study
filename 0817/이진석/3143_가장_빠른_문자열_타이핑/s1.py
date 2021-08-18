for tc in range(1, int(input())+1):
    string, target = input().split(' ')
    cnt = 0
    i = 0
    while i < len(string):
        if i < len(string)-len(target)+1 and string[i:i + len(target)] == target:
            cnt += 1
            i += len(target)
        else:
            cnt += 1
            i += 1
    print('#{} {}'.format(tc, cnt))