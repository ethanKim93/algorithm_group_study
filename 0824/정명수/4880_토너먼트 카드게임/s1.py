import sys
sys.stdin = open('input.txt')
def winner(s):
    for key,value in s.items():
        if value:


def rsp(s):
    if len(s) == 1:
        return s
    elif len(s)==2:
        return winner(s)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    people = list(map(int,input().split()))
    print(people)