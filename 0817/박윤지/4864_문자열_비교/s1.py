import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0  # 결과를 저장할 변수
    for i in range(0, len(str2) - len(str1) + 1):  # 인덱스 0부터 끝까지 str1이 있는지 확인할 수 있도록 범위 설정
        if str2[i:i+len(str1)] == str1:  # str1의 크기만큼 slicing해서 str1과 같은 값인지 검사
            result = 1
            break  # 같은 부분이 하나만 있어도 되기 때문에 뒤는 검사하지 않고 for문을 끝냄
    print('#{} {}'.format(tc, result))