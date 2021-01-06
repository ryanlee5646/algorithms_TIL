
Data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

Mymap = [[0]*8 for i in range(8)]
Queue = [0] * 1000
visited = [0] * 8
Distance = [-1] * 8
Parent = [-1] * 8
front = -1
rear = -1

def BFS(here):
    global front, rear
    rear+=1
    Queue[rear] = here
    visited[here] = True
    while front!= rear:
        front+=1
        here = Queue[front]


        for next in range(8):
            if Mymap[here][next] and not visited[next]:
                visited[next] = True
                Distance[next] = Distance[here] + 1
                Parent[next] = here
                rear += 1
                Queue[rear] = next


for i in range(0,len(Data),2):
    Mymap[Data[i]][Data[i+1]] = 1
    Mymap[Data[i+1]][Data[i]] = 1


Distance[1] = 0
BFS(1)

print(Distance)
print(Parent)
