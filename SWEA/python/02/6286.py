# 리스트 내포 가능을 이용해 피보나치 수열 10번째까지 출력하는 프로그램을 작성하십시오.

l = []
for i in range(10):
    if i < 2:
        l.append(1)
    else:
        l.append(l[i-1]+l[i-2])
print(l)
