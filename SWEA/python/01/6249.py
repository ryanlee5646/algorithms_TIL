# 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
num = list(input())
l = [0,0,0,0,0,0,0,0,0,0]
for i in num:
    l[int(i)] += 1
for i in range(10) :
    print(i,end=' ')
print()
for i in l:
    print(i,end=' ')



num = list(input())
num_list = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, 
"6":0, "7":0, "8":0, "9":0}
for i in num:
    for j in num_list.keys():
        if i == j:
            num_list[i]+=1
print(' '.join(num_list.keys()))
print(' '.join(list(map(str,num_list.values()))))