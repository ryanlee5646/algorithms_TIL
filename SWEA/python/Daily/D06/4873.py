import sys
sys.stdin = open("4873.txt", "r")

T = int(input())

for t in range(T):
    word = list(map(str, input()))
    i = 0
    while i < len(word)-1 :
        if word[i] == word[i+1]:
            word.pop(i+1)
            word.pop(i)
            i=0
        else:
            i+=1

    print(f'#{t+1} {len(word)}')
