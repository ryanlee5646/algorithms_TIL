import sys

sys.stdin = open('input.txt', 'r') # 파일에서 읽을 때 사용

# Data = list(map(int, input().split()))


# 3 4 1 2 5  ->  3 4 1 5 2

def next_permutation(Data):
    for Now in range(len(Data)-1):
        Next = Now + 1
        if Data[Now] < Data[Next]:
            cand1 = Now
    if cand1 == 0:
        return False
    cand2 = len(Data) -1
    while Data[cand1] > Data[cand2]:
        cand2 -= 1

    Data[cand1], Data[cand2] = Data[cand2], Data[cand1]

    Data[cand1+1:] = Data[:cand1:-1]
    return(Data)

Data = list(map(int, input().split()))

if next_permutation(Data):
    print(Data)
else:
    print("마지막 순열입니다.")





