# import sys
# sys.stdin = open('input.txt', 'r')
ans = 0

def GetSome(here):
    global ans
    if here==howmany:
        ans+=1
        return
    if here > howmany :
        return
    GetSome(here+1)
    GetSome(here+2)

howmany = int(input())

start = 0

GetSome(start)

print(ans)