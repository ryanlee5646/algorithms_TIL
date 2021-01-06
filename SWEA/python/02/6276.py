# 다음의 결과와 같이 구구단 2단부터 9단의 결과값 중에 3의 배수거나 7의 배수인 수를
# 제외한 값을 리스트 객체 result 안에 각 단마다 리스트를 만들어 삽입하고 이를 출력하십시오.

l1 = []
for i in range(2,10):
    l2 = []
    for j in range(1,10):
        if not ((i*j) % 3 ==0 or (i*j) % 7 == 0):
            l2.append(i*j)
    l1.append(l2)
        
print(l1)
