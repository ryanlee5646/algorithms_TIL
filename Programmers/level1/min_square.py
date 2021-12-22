# Level1 최소직사각형

def solution(sizes):
    max_arr = []
    min_arr = []
    
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            max_arr.append(sizes[i][0])
            min_arr.append(sizes[i][1])
        else:
            max_arr.append(sizes[i][1])
            min_arr.append(sizes[i][0])
            
    return max(max_arr) * max(min_arr)