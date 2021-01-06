# while문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
a = '*'
count = 5
star = 7
while count > 0:
    count  -= 1
    print(f'{(a*star):^7}')
    star -= 2

i = 5
while i > 1:
	i -= 1
	print((' ' * (4 - i) + ('*' * (i * 2 - 1) )))



j =0
n=0
while j != 4:
    print(" "*n+"*"*(7-2*j)+" "*n)
    j += 1
    n += 1



# print((' '*5) + ('*'*1))
# print((' '*4) + ('*'*3))
# print((' '*3) + ('*'*5))
