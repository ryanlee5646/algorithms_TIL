def make_binary(N):
    global number
    index=3
    while index>=0:
        number[index]=N%2
        N=N//2
        index-=1

data='01D06079861D79F99F'
binary=[]

for i in data:
    number=[0,0,0,0]
    if ord(i)<65:
        make_binary(int(i))
    else:
        N=ord(i)-65+10
        make_binary(N)
    for n in number:
        binary.append(n)

t=0
for i in range(len(binary)):
    t=2*t+binary[i]
    if (i+1)%7==0:
        print(t)
        t=0
    elif len(binary)==i+1:
        print(t)
