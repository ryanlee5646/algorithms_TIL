import sys
sys.stdin = open("pirme_num.txt", "r")

Num1,Num2 = map(int, input().split())
prime_list = [x for x in range(Num1, Num2+1)]
print(prime_list)
# for i in range(1,10):
#
