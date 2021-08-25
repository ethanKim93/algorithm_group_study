import sys
import copy
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    student = list(map(int, input().split()))
    student2 = copy.deepcopy(student)
    print(N)
    while len(student) >= 0:
        print(len(student))
        if len(student) == 1:
            break
        elif len(student) != 2:
            for i in range(N//2):
                if student[i] - student[i + 1] == -2 or student[i] - student[i + 1] == 1:
                    print('i가 이겨서 +1 삭제 ')
                    student.pop(i + 1)
                elif student[i] - student[i + 1] == 0:
                    print('비겨서 큰 숫자 삭제')
                    student.pop(i + 1)
                elif student[j] - student[j + 1] == -1 or student[j] - student[j + 1] == 2:
                    print('i가 져서 i 삭제')
                    student.pop(i)
        else:
            j = 0
            print(len(student))
            if student[j] - student[j + 1] == -2 or student[j] - student[j + 1] == 1:
                print('i가 이겨서 +1 삭제 ')
                student.pop(j + 1)
            elif student[j] - student[j + 1] == 0:
                print('비겨서 큰 숫자 삭제')
                student.pop(j + 1)
            elif student[j] - student[j + 1] == -1 or student[j] - student[j + 1] == 2:
                print('i가 져서 i 삭제')
                student.pop(j)
    print('#{} {}'.format(tc + 1, student2.index(student[0]) + 1))