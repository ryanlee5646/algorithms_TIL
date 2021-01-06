# 리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
l = []
for i in range(5):
    a = int(input())
    l.append(a)
print(f'입력된 값 {l}의 평균은 {sum(l)/5}입니다.')    
