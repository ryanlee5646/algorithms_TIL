# 방법 1
num = int(input())
front = 0
rear = num-1
Queue = [0] * 1000
for i in range(1,num+1):
    Queue[i-1] = i
print(Queue)

for i in range(num-2): # 2명이 남아야 하므로 입력값보다 2번 적게 돌림
    rear += 1
    Queue[rear] = Queue[front]
    front += 1

    rear += 1
    Queue[rear] = Queue[front]
    front += 1
    front += 1

print(Queue)
print(Queue[front])
print(Queue[rear])
