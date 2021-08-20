import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    length, password = input().split()
    length = int(length)
    pas=''
    for i in range(length):
        if pas:
            if pas[-1] == password[i]:
                pas = pas[:-1]
            else:
                pas += password[i]
        else:
            pas = password[i]
    print('#{} {}'.format(tc,pas))
