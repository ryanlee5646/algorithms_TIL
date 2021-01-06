import sys
sys.stdin = open("str.txt", "r")

T = int(input())

def kmp(pattern, target):
    pi = [0] * len(pattern)
    pi[0], pi[1] = -1, 0
    i,j = 0, 1
    while j < len(pattern)-1:
        if pattern[i] == pattern[j]:
            pi[j+1] = pi[j] + 1
            i+=1
            j+=1     
        elif pattern[i] != pattern[j]:
            if pattern[0] == pattern[j]:
                pi[j+1] = pi[j]
            else: 
                pi[j+1] = 0
                i = 0
            j+=1
    p = 0  # 문자열 비교 위치      
    while p < len(target) - len(pattern)+1: # 
        count = 0
        for i in range(len(pattern)):
            if pattern[i] == target[p+i]:
                count += 1
            else:
                break
        if count == len(pattern):
            return True

        else:
            p += count - pi[count]



for t in range(1,T+1):
    pattern = input()
    target = input()
    
    if kmp(pattern, target):
        print('#%d 1' %(t))
    else:
        print('#%d 0' %(t))
