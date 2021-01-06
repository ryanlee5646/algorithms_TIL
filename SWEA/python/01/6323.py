# 다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
# 입력 : 10    출력: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def fibo(num = int(input())):
    num_list = []
    for i in range(num):
        if i < 2:
            num_list.append(1)
        else:
            num_list.append(num_list[i-1]+num_list[i-2])
    return num_list
print(fibo())
            
#             n=13
# a=0;b=1
# print('0', end='')
# while b<=n:
#     print(', %d'%b, end='')
#     a,b = b,a+b

# num = int(input())
# print(len(list(range(num+1))))


    # num_list = list(range(int(input())))