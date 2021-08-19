import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    stack = [1, 3]  # 초기 값 입력
    for i in range(2, N//10):
        result = stack[i-1] + stack[i-2] * 2    # 전체길이 i를 만드려면 i-1짜리 1개, i-2짜리 2개가 필요(ㅁ,ㅣ,=)
        stack.append(result)

    print("#{} {}".format(tc, result))