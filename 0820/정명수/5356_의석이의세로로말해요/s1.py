import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1,T+1):
    li=[]
    max_sent=0
    for _ in range(5):
        sent = input()
        li.append(sent)
        if len(sent)>max_sent:
            max_sent = len(sent)
    sentence =''
    for i in range(max_sent):
        for j in range(5):
            try:
                if len(li[j]) >= i:
                    sentence += li[j][i]
            except:
                pass
    print('#{} {}'.format(tc,sentence))