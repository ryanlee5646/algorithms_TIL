# 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 
# 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오.
a = []
for num in range(100, 301):
    if num // 100 == 2: #100의자리 짝수
        if ((num % 100) // 10) % 2 == 0:
            if num % 2 == 0:
                a.append(num)
b = map(str, a)
print(','.join(b))