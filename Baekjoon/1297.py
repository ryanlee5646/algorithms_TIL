# TV 크기   
cross, h_rate, w_rate = map(int, input().split())

# 대각선 비율 구하기
cross_rate = (cross**2 / (h_rate**2 + w_rate**2)) ** 0.5

width = int(cross_rate * w_rate)
            
height = int(cross_rate * h_rate)

print(height, width , end='' )