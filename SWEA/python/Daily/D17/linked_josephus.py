class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

def Enqueue(num):
    global head
    newNode = Node(num)
    if head == None:
        head = newNode
    else: #순차적으로 넣으면 되니까 비교할 필요 없음
        p = head
        while p.link != None:
            p = p.link
        p.link = newNode
head = None

people = [_ for _ in range(1,5)]
print(people)

for i in range(1, len(people)+1):
    Enqueue(i)

p = head
while p.link:
    p = p.link
p.link = head

life = len(people)
p = head

while True:
    p.link.link = p.link.link.link
    p = p.link.link
    life -= 1
    if life == 2:
        break

for i in range(2):
    print(p.data)
    p = p.link

# N = 41
# people = [0] * 41
# for i in range(5):
#     people[i] = Node(i)
#     if i > 0:
#         people[i - 1].link = people[i]
# people[i].link = people[0]
#
# p = people[0]
# while p.link.link != p:
#     p.link.link = p.link.link.link
#     p = p.link.link
#
# print(p.data + 1)
# p = p.link
# print(p.data + 1)