import sys
sys.stdin = open('input.txt')

switch = int(input())
# 스위치의 개수
switch_arr = list(map(int, input().split()))
# 1은 켜진 것, 0은 꺼진 것
students = int(input())
# 학생 수
for _ in range(students):
    gender, idx = map(int, input().split())
# 1은 남학생, 2는 여학생, 그 옆에 숫자는 학생이 받은 수
    if gender == 1:
        for i in range(1, (len(switch_arr) // idx) + 1):
            if switch_arr[(idx * i) - 1] == 0:
                switch_arr[(idx * i) - 1] = 1
            else:
                switch_arr[(idx * i) - 1] = 0

    if gender == 2:
        if switch_arr[(idx - 1)] == 0:
            switch_arr[(idx - 1)] = 1
        else:
            switch_arr[(idx - 1)] = 0
        left = idx - 2
        right = idx
        while left >= 0 and right < switch and switch_arr[left] == switch_arr[right]:
            if left < 0 or right >= switch:
                break
            if switch_arr[left] == 0:
                switch_arr[left], switch_arr[right] = 1, 1
            elif switch_arr[left] == 1:
                switch_arr[left], switch_arr[right] = 0, 0
            left -= 1
            right += 1

cnt = 0
ans = ''
for i in range(switch):
    ans += (str(switch_arr[i]) + ' ')
    cnt += 1
    if cnt == 20:
        print(ans)
        ans = ''
        cnt = 0
if len(ans) != 0:
    print(ans)

#01110101
#10001101
