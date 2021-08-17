import sys
sys.stdin = open("test_input.txt", "rt", encoding="UTF8")

for _ in range(10):
    test = int(input())

    find_str = str(input())
    looking_str = str(input())
    n = len(find_str)   # 찾을 문자열의 길이를 저장해둡니다.
    cnt = 0

    for i in range(len(looking_str)):
        if looking_str[i] == find_str[0]:
            if looking_str[i:i+n] == find_str:
                cnt += 1

    print('#{} {}'.format(test, cnt))
