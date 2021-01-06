
Fibo = [-1] * 101
Fibo[0] = 0
Fibo[1] = 1

for now in range(2,101):
    Fibo[now] = Fibo[now-1] + Fibo[now-2]

print(Fibo[7])

def fibo(num):
    if Fibo[num] == -1:
       Fibo[num] = fibo(num-1) + fibo(num-2)
       return Fibo[num]
    else:
        return Fibo[num]

for i in range(1,10):
    print(fibo(i), end=' ')