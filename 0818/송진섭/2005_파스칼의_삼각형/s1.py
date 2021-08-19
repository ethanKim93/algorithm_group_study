import sys
sys.stdin = open('input.txt')

pascal_list = [[] for _ in range(11)]  # 빈 이중리스트
pascal_list[0] = [0]  # 인덱스로 접근하기위해 0에는 0입력
pascal_list[1] = [1]  # 1번째 출력할 리스트
pascal_list[2] = [1, 1]  # 2번째 출력할 리스트

for i in range(3, 11):  # 3번째 부터는 [1, 이전 리스트의 원소들의 합, 1]로 구성
    pascal_list[i].append(pascal_list[1][0])  # 처음에는 1 삽입
    pascal_list[i] += [pascal_list[i-1][j]+pascal_list[i-1][j+1] for j in range(len(pascal_list[i-1])-1)]
    pascal_list[i].append(pascal_list[1][0])  # 끝에는 1 삽입

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print('#{}'.format(tc))
    for i in range(1, N+1):
        print(*pascal_list[i])  # pascal_list에 답이 담겨 있기 때문에 해당 인덱스 출력

