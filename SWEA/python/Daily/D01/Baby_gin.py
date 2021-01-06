# 접근방법
# 일단 Counting_sort를 이용해서 입력받은 숫자를 카운트한 스트를 만들어서
# 인덱스(n , n+1, n+2)를 통해 연속하는 같은 수(run) 이거나
# 하나의 인덱스에 3개이상의 숫자(triple)가 있는지 파악

Data =list(map(int, input().split()))
Count = [0] * (max(Data)+1)
if len(Data) < 7: # 카드를 6장만 뽑을 수 있음
    for data in Data: # 뽑은 카드를 인덱스 == 카드숫자로 뽑은 개수를 정렬
        Count[data] += 1
print(Count)
triplet = 0
run = 0
for index, count in enumerate(Count): # triplet를 구하는 알고리즘
    if count > 2:
        Count[index] -= 3
        triplet += 1
for index in range(len(Count)-2): # run을 구하는 알고리즘
    if Count[index]+Count[index+1]+Count[index+2] >= 3:
        Count[index] -= 1
        Count[index+1] -= 1
        Count[index+2] -= 1
        run += 1
if triplet + run ==2:
    print('baby_gin입니다!')
else:
    print('baby_gin이 아닙니다!')

    
        



[1,1,1,2,3,4]

[0,3,1,1,1,0]