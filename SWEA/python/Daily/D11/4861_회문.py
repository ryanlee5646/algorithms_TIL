import sys
sys.stdin = open("4861_회문.txt", "r")

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split()) 
    # N줄의 N개의 문자열
    My_map = []
    
    for i in range(N):
        data = input()
        My_map.append(data)
    for y in range(N):
        string_1 = ''
        string_2 = ''
        for x in range(N):
            string_1 += My_map[y][x] #가로
            string_2 += My_map[x][y] #세로

        for k in range(N-M+1):
            a = string_1[k:M+k]
            b = a[::-1]
            if a == b:
                print("#{} {}".format(t,a) )
        for j in range(N-M+1):
            c = string_2[j:M+j]
            d = c[::-1]
            if c == d:
                print("#{} {}".format(t,c) )
        
   
        