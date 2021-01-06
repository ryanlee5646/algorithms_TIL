from copy import deepcopy
def arrow(person):
    global cnt, died
    #왼
    for distance in range(1, d + 1):
        for dir in range(1,distance+1):
            ny = (h - 1) - (dir)
            nx = person - (distance - dir)
            if  0<=ny<h-1 and 0<=nx<w and record[ny][nx]==1:
                if (ny,nx) not in died:
                    cnt +=1
                    died += [(ny,nx)]
                    return
                else:
                    return
    #오
        for dir in range(distance - 1, 0, -1):
            ny = (h - 1) - (dir)
            nx = person + (distance - dir)
            if 0 <= ny < h-1 and 0 <= nx < w and record[ny][nx] == 1:
                if (ny, nx) not in died:
                    cnt += 1
                    died += [(ny, nx)]
                    return
                else:
                    return

h,w,d = map(int,input().split())
original = [list(map(int,input().split())) for i in range(h)] + [[0]*w]
h = h+1
mymax = -1
all_died = [[0]*w for i in range(h)]

for first in range(w-2):
    for second in range(first+1, w-1):
        for third in range(second+1,w):
            cnt = 0
            sample_original = deepcopy(original)
            time = 0
            while sample_original!=all_died :
                died = []
                record = deepcopy(sample_original)
                arrow(first)
                arrow(second)
                arrow(third)
                for i in died:
                    record[i[0]][i[1]]=0
                for i in range(h-1):
                    if time>=i:
                        sample_original[i]=[0]*w
                    else:
                        sample_original[i]=record[i-1]
                time+=1
            if cnt > mymax:
                mymax=cnt
print(mymax)