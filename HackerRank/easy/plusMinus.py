import sys
print(sys.path)
sys.stdin = open('input/plusMinus1.txt','r')

def plusMinus(arr):
    positive = negative = zero = 0

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print(positive)
    print(negative)
    print(zero)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))




    plusMinus(arr)