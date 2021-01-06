data = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
_data = [[-1,-1,-1,-1,-1] for x in range(5)]

def issafe(x,y,n) :
    return x >= 0 and x < n and y >= 0 and y < n and _data[y][x] == -1

def min_pop(data) :
    resultx = resulty = 0
    item = 999
    for i in range(5) :
        for j in range(5) :
            if data[j][i] == 999 :
                continue
            if data[j][i] < item :
                resulty = j
                resultx = i
                item = data[j][i]
    data[resulty][resultx] = 999
    if item == 999 :
        return False
    return item

dx = [1,0,-1,0]
dy = [0,1,0,-1]
k = 0
x = y = 0
for j in range(25) :
    item = min_pop(data)
    if item :
        _data[y][x] = item
        if not issafe(x+dx[k],y+dy[k],5) :
            k += 1
            k %= 4
        x+= dx[k]
        y+= dy[k]

print(_data)


