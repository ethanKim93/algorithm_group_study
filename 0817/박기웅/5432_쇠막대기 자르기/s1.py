import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    batch = input()
    i = cnt = steel = 0
    while(i<len(batch)):
        if batch[i:i+2] =='()': #레이저가 나오면 누적된 steel 개수를 cnt에 더해주고, 2칸 이동
            cnt += steel
            i += 2
        elif batch[i] == '(': #레이저가 아닌 열린 괄호가 나오면 steel 개수 추가, 1칸 이동
            steel += 1
            i += 1
        else: # 나머지 닫힌 괄호의 경우 steel 개수를 줄여주고 cnt에 1추가 후 다음 칸 이동
            steel -= 1
            cnt += 1
            i += 1

    print('#{} {}'.format(tc, cnt))