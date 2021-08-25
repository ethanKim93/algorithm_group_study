import sys
sys.stdin = open("input.txt")

# 원형 큐 형태의 풀이

while True:
    try:
        tc = int(input())
        password = list(map(int, input().split()))
        front = 0
        rear = 7

        flag = True
        while flag:
            for i in range(1, 6):
                temp = password[front]
                front = (front + 1) % 8
                rear = (rear + 1) % 8
                if temp - i <= 0:
                    password[rear] = 0
                    flag = False
                    break
                password[rear] = temp - i
        print("#{}".format(tc), end=" ")
        for idx in range(front, front + 8):
            print(password[idx % 8], end = " ")
        print()
    except :
        break