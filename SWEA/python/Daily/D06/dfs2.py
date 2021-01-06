def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    if top == -1:
        return 0
    x = stack[top]
    top -= 1
    return x

def findnext(here):
    for next in range(8):
        if MyMap[here][next] and not visited[next]:
            return next

def DFS(here):
    global top
    print(here)
    visited[here] = True

    next = findnext(here)
    if next:
        push(here)
    while next:
        here = next
        print(here)
        visited[here] = True
        next = findnext(here)
        push(here)
    here = pop()

Data = list(map(int, input().split()))
howmany = int(len(Data) /2)