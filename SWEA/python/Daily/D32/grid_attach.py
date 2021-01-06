import sys
sys.stdin = open("grid_attach.txt", "r")

# def IsSafe(y,x,N):
#     if 0<=y<N and 0<=x<N:
#         return True
#     else:
#         return False
# def DFS(y,x,temp,length):
#     if length == 7:
#         if not temp in string:
#             string.append(temp)
#         return
#     for i in range(4):
#         newy = y+dy[i]
#         newx = x+dx[i]
#         if IsSafe(newy,newx,N):
#             DFS(newy,newx,temp+data[newy][newx],length+1)
# dy = [1,0,-1,0]
# dx = [0,1,0,-1]
# T = int(input())
# for t in range(1,T+1):
#     N = 4
#     data = [list(map(str,input().split())) for i in range(N)]
#     string = []
#     for y in range(4):
#         for x in range(4):
#             DFS(y,x,data[y][x],1)
#     print("#{} {}".format(t,len(string)))

def IsSafe(y,x,N):
    if 0<=y<N and 0<=x<N:
        return True
    else:
        return False
def DFS(y,x,temp,length):
    global num_list
    if length == 7:
        if not temp in num_list:
            num_list += [temp]
        return
    for i in range(4):
        newy = y+dy[i]
        newx = x+dx[i]
        if IsSafe(newy,newx,N):
            DFS(newy,newx,temp*10+data[newy][newx], length+1)
dy = [1,0,-1,0]
dx = [0,1,0,-1]
T = int(input())
for t in range(1,T+1):
    N = 4
    data = [list(map(int,input().split())) for i in range(N)]
    num_list = []
    for y in range(4):
        for x in range(4):
            DFS(y,x,data[y][x],1)
    print(num_list)
    print("#{} {}".format(t,len(num_list)))
