import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    str1_dict = {} # str1의 문자를 담고 있는 딕셔너리, 개수는 0으로 초기화
    for s in str1:
        str1_dict[s] = 0

    for s in str2: # str2의 문자열을 돌면서 있으면 하나씩 추가 없으면 pass
        try: str1_dict[s] += 1
        except: pass

    max_s = 0
    for value in str1_dict.values():
        if max_s < value:
            max_s = value
    print('#{} {}'.format(tc, max_s))


