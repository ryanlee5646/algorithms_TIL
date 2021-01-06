import sys
sys.stdin = open("gcd_lcm.txt", "r")

Num1, Num2 = map(int,input().split())
small = 0
max_num = 0
if Num1>Num2:
    small = Num2
else:
    small = Num1
if small > 0:
    for i in range(1,small+1):
        if Num1%i == 0 and Num2%i == 0:
            if i > max_num:
                max_num = i
print(max_num)
print("{}".format((Num1*Num2)//max_num))