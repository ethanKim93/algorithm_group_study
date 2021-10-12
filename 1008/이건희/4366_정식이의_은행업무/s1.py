import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1,t+1):
    b = input()
    t = input()
    temps2 = []
    for i in range(len(b)):
        temps = int(b,2) ^ (1<<i)
        temps2.append(temps)

    t_dic = {"0":["1","2"], "1":["0","2"], "2":["0","1"]}
    temps3 = []
    for i in range(len(t)):
        for x in t_dic[t[i]]:
            temps = t[:i] + x + t[i+1:]
            temps3.append(int(temps,3))

    for i in temps2:
        if i in temps3:
            break
# Pass